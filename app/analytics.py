import polars as pl

lazy_df = pl.scan_csv("cleaned_transactions.csv")

lazy_df = lazy_df.with_columns([
    pl.col("txn_ts").str.to_datetime().alias("txn_ts"),
    pl.col("txn_ts").str.to_datetime().dt.date().alias("date")
])

lazy_df = lazy_df.filter(
    pl.col("amount") > 1000
)
lazy_df = lazy_df.with_columns(
    (pl.col("amount") * 1.18).alias("amount_with_tax")
)
daily_totals = (
    lazy_df
    .group_by(["account_id", "date"])
    .agg(
        pl.col("amount").sum().alias("daily_total")
    )
    .sort(["account_id", "date"])
)
daily_totals = daily_totals.with_columns(
    pl.col("daily_total")
    .rolling_sum(window_size=7)
    .over("account_id")
    .alias("rolling_7day_sum")
)

result = daily_totals.collect()

print(result)