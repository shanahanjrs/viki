# Viki

### Viki job automation platform command line tool

## Features of Viki
- Simple to start up and use
- Small and lightweight
- Trigger a job run automatically via Webhook or manually with the command line tool
- Uses JSON instead of XML

## Installing
Pip installation:
```
pip install viki
```

For development:
```
$ git clone https://github.com/shanahanjrs/viki
$ cd viki
$ pip3 install -e .
```

## FAQ

### How do I use the command line tool?
`$ viki -h` will produce and output similar to:

```
usage: viki [-h] [--host HOST] [--port PORT] [--json] [-V] [-v] ...

positional arguments:
  {list,run,create,output}

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           Vikid host to connect to (default: "http://localhost")
  --port PORT           Port to connect to Vikid host on (default: "5000")
  --json                Show output as json (default: False)
  -V, --verbose         Verbose execution details (default: False)
  -v, --version         Display viki version
```

By default `viki` will look for the daemon locally on port 5000, if you are connecting to a remote server you will have to specify the location:

`$ viki list --host example.com --port 8080`

### Will there be Windows support any time soon?
At the moment there is no plan to support windows operating systems.

### License
Code released under the [Apache 2.0 License](https://github.com/shanahanjrs/viki/blob/master/LICENSE.md).
