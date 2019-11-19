# catfact-notifier
A cool snippet to display a catfact inside a notification on MacOS and Unix systems.

# How does it work?
The script *catfact.py* fetches a random fact about cats from the [*Cat Facts API*](https://catfact.ninja/).

One can trigger it manually, assuming your system is up with python 3:

```
$ python catfact.py
```

Another way to use it is to pass on the triggering to a cron task. For example, to display a catfact each hour, install the following task in your crontab:

```
@hourly /usr/local/bin/cat-notify.sh
```
