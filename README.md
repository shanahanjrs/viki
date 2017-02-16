# Viki

### Job automation platform

## Features of Viki
- Simple to start up and use
- Small and lightweight
- Trigger a job run automatically via Webhook or manually with the command line
- Uses JSON instead of xml for data formatting

## Installing
Normal installation:
```
pip install viki
```

For development:
```
$ git clone https://github.com/shanahanjrs/viki
$ cd viki; pip3 install -e .
```

## FAQ

### How do I start the Viki daemon?
Simple, run `$ vikid` to start the daemon. Starting with supervisor recommended.

### How do I use the command line tool?
By using `$ viki` you can see a list of possible options to use Viki and even generate the system files needed for it to run.

### Will there be Windows support any time soon?
At the moment there is no plan to support windows based operating systems. Linux/OSx only at the time.

## License

Code released under the [Apache 2.0 License](https://github.com/shanahanjrs/viki/blob/master/LICENSE.md).
