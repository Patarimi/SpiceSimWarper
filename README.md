# `pywas`
*Py*thon *W*rapper for *A*nalog design *S*oftware

**Installation using [pipx](https://pypa.github.io/pipx/installation/)**:

```console
$ pipx install pywas
```

**Usage**:

```console
$ pywas [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* For a given wrapper:
  * `install`: install the software on the system.
  * `prepare`: not implemented yet. Set everything up for the next simulation.
  * `run`: run the simulation and store the output in results.
  * `export`: export the results as a .hdf5 file.
