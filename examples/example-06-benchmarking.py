#!/usr/bin/env python3
#
# This script demonstrates the usage of different benchmarking tools. It contrasts native optimization by an actual database
# system to a defensive optimization scheme using the UES algorithm
#
# Requirements: a running IMDB instance on Postgres with the connect file being set-up correctly. This can be achieved using
# the utilities in the root postgres directory.
#

from postbound import postbound as pb
from postbound.db import postgres
from postbound.experiments import workloads, runner
from postbound.optimizer import presets

# Setup: we optimize queries from the Join Order Benchmark on a Postgres database
postgres_db = postgres.connect()
job_workload = workloads.job()

# Configure the optimization pipeline for UES
ues_settings = presets.fetch("ues")
ues_pipeline = pb.TwoStageOptimizationPipeline(postgres_db).load_settings(ues_settings).build()

# Execute the benchmarks: each query should be repeated 3 times and each workload should be repeated 3 times as well
# After each workload repetition, the execution order of all queries should be changed. Finally, all queries should be executed
# as COUNT(*) queries
query_preparation = runner.QueryPreparationService(count_star=True)

# Benchmark the native workload
native_results = runner.execute_workload(job_workload, postgres_db,
                                         workload_repetitions=3, per_query_repetitions=3, shuffled=True,
                                         query_preparation=query_preparation, include_labels=True)

# Benchmark the UES workload
ues_results = runner.optimize_and_execute_workload(job_workload, ues_pipeline,
                                                   workload_repetitions=3, per_query_repetitions=3, shuffled=True,
                                                   query_preparation=query_preparation, include_labels=True)
