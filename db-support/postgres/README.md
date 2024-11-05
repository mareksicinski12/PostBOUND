# Postgres management

This folder provides utilities to

- build a Postgres server instance from source `postgres-setup.sh`. Check with `--help` for details
- install a number of recommended and/or required extensions (this is also handled as part of the general Postgres setup)
- manage an installed Postgres server (start via `postgres-start.sh` and stop via `postgres-stop.sh`)
- import popular benchmark databases via the <code>workload-_\<benchmark name\>_-setup.sh</code> scripts. Use `--help` to see supported options

Notice that the Postgres setup performs a _local_ installation, no global paths or public
directories are modified. Therefore, use the `postgres-load-env.sh` utility to setup you `PATH`
environment variable correctly for the current session. The `-start`, `-stop` and `-setup`
scripts can also be sourced to keep the `PATH` up to date (i.e. adding the Postgres binaries
to the `PATH` upon server start and removing them again afterwards). If the Postgres server
was installed to a custom location, this location has to be supplied when calling the
management scripts.

Finally, the `postgres-psycopg-setup` utility generates a config file that can be used by
PostBOUND's database interaction code to automatically connect to the database. See the
documentation in `postgres.py` for details.

The `util` directory contains a collection of stored procedures for different introspection methods.

