# kitt4sme.fams-sim

> Sneakily pretends to be FaMS.


### Hacking

Install Python (`>= 3.8`), Poetry (`>=1.1`) and the usual Docker
stack (Engine `>= 20.10`, Compose `>= 2.1`). If you've got Nix, you
get a dev shell with the right Python and Poetry versions simply by
running

```console
$ nix shell github:isteps-sps-lab/kitt4sme.fams-sim?dir=nix
```

Otherwise, install the usual way you do on your platform. Then clone
this repo, `cd` into its root dir and install the Python dependencies

```console
$ git clone https://github.com/isteps-sps-lab/kitt4sme.fams-sim.git
$ cd kitt4sme.fams-sim
$ poetry install
```

Finally drop into a virtual env shell to hack away

```bash
$ poetry shell
$ charm .
# ^ Pycharm or whatever floats your boat
```

Build and run the Docker image

```console
$ docker build -t kitt4sme/fams-sim .
$ docker run -e POOL_SIZE=5 -e SAMPLES_N=300 -e SAMPLING_RATE=1.0 -e TENANT=demo -e ORION_URI=http://localhost:1026 ITERATIONS=5 kitt4sme/fams-sim
```
> NOTE: set ITERATIONS = -1 for a never ending simulation.

### Live simulator

This test bed simulates a live environment similar
to that of the KITT4SME cluster. In the `famssim` directory, you'll find
two Docker compose files with:

* Orion LD connected to MongoDB
* Quantum Leap with a CrateDB (or Timescale) backend

To start the show, run (Ctrl+C to stop)

```console
$ poetry shell
$ python famssim/tests/sim <crate|timescale>
```

This will bring up the Docker compose environment (assuming you've
got a Docker engine running already), subscribe Quantum Leap to Orion
and then will start sending Wearable and Worker entities to Orion.
On receiving those entities, Orion forwards them to Quantum Leap.
Notice that all those entities do not belong to a tenant.

#### (only if using CrateDB)

Browsing to the [CrateDB Web UI](http://localhost:4200) you should 
be able to query both the entities tables to see data coming in 
from the simulator through Orion and then Quantum Leap.
