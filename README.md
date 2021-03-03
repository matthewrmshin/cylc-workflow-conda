# Cylc Work Flow With Tasks Running In A Conda Envvironment

## Installation

### Set Up Conda

Install Miniconda, if not already done. Follow the instruction at:
[Install Miniconda on Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)

Configure Conda to use e.g. Artifactory for a more secure experience.

## Running the Cylc Work Flow

Assume:

* Cylc and Rose already installed in your environment.
* Suite Running on Linux environment, with tasks submitted via SLURM.

Usual commands:

```sh
# Adjust name to suit purpose
NAME=hello

# To start the suite from a work tree of this project
rose suite-run -n ${NAME}

# To stop a suite
cylc stop "${NAME}"  # Schedule stop when all tasks are done
cylc stop --kill "${NAME}"  # Kill tasks and stop
cylc stop --now "${NAME}"  # Stop suite now

# To start a brand new run
rose suite-run --new -n ${NAME}  # add more arguments as required

# To clean the locations created by a suite
rose suite-clean -y "${NAME}"
```

Cylc Locations:

* Run directory: `~/cylc-run/${NAME}/`
* Conda environment: `~/cylc-run/${NAME}/share/opt/condaenv/`

## How it works

USER_CONDA_PROFILE: An environment variable that points to the script to
initialise Conda. (Default is under the normal location in your HOME directory.)

SUITE_CONDA_ENV: An environment variable to define the location to install a
Conda environment under CYLC_SUITE_SHARE_DIR.

The `install_condaenv` task runs the `bin/install-condaenv` script to
install/update the suite's Conda environment using an `environment.yml` file.
It also installs any Python libraries stored with the suite into the Conda
environment by running the `python3 ./setup.py install`.

The CONDA family is inherited by any tasks that need to run with the suite's
Conda environment.
* It uses a `pre-script` to initialise Conda and activate the suite's Conda environment.
