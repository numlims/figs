# figs

fhir getters (and setters?) for cxx.

```
import figs.specimen as figs
res = figs.resource(my_fhir_entry)
sampleid = figs.sampleid(res)
```

api doc [here](https://numlims.github.io/figs/).

## install

download figs whl from
[here](https://github.com/numlims/figs/releases). install whl with
pip:

```
pip install figs-<version>.whl
```

## dev

edit [`figs/main.ct`](./figs/main.ct) and [`figs/init.ct`](./figs/init.ct).

generate the code from ct with [ct](https://github.com/tnustrings/ct) or [ct for vscode](https://marketplace.visualstudio.com/items?itemName=tnustrings.codetext).

build and install:

```
make install
```

test:

```
make test
```
