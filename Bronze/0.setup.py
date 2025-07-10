# Databricks notebook source
# MAGIC %sql
# MAGIC create catalog if not exists flights
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists flights.raw
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create volume if not exists flights.raw.rawvolume

# COMMAND ----------


dbutils.fs.mkdirs("/Volumes/flights/raw/rawvolume/rawdata/airports")

# COMMAND ----------

# MAGIC %sql
# MAGIC create volume if not exists flights.bronze.bronzevolume