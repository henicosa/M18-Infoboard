# Digital Infoboard
This is the open source repository of the M18's digital information board. Currently the state of the board is work in progress.

## Install for Hosting (Not Development)
1. Clone the repository 
2. Alter the `application.json` to your needs
3. Run the `start.sh` script on any Linux device.

The `start.sh` script will install a docker image and run a docker container on your device with the default port 5343.

The `stop.sh` script stop the currently running docker container.


## Development
You don't need to run the docker container for development purpose. Instead just install the python requirements listed in the `requirements.txt` with `pip3 install -r requirements.txt`. Then you can either run `python app.py` or `python -m flask run` in the project root directory to start the web application on local port 5000.

### Python Dependencies
If you import new packages during development make sure to add them to the `requirements.txt`. The name that you used to install the package with pip is sufficient, although it is recommended, you do not need to add the specific version. Alternatively you can use pipreqs in the root directory with `pipreqs . --force` that will update `requirements.txt` based on your source code.

### Logging
Please log important events in your code. This project makes use of the python logging library. Logs will be written to the `app/log/application.log` file and can be viewed in the web application via the `/logs` route. First import the applog file in the beginning with `import applog`then you can log events by calling
- `applog.debug("YOUR MESSAGE")`
- `applog.info("YOUR MESSAGE")`
- `applog.warning("YOUR MESSAGE")`
- `applog.error("YOUR MESSAGE")`

The logged events will also get printed on the console.

### Crawler
Add Crawler scripts in the folder `crawler/` and integrate them in `feed.py`.