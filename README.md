# Brackets

  
# Developer Workstation Setup
This Skyfit repository uses Node.js version 4.5.0 so install nvm in order to ensure that you are using the correct version.

1. Make sure all the prerequisites are installed (see below).
2. Clone this repo and switch into node version 4.5.0
	```
  	git clone https://github.com/skyfit/Skyfit.git
  	nvm use 4.5
	```

3. Make sure that you have the 'config.local.coffee' file and that line 53 says:

	```
	SHOW_KUE_UI: false
	```
4. Install all the dependencies

	```
	npm install
	```
5. Run it

	```
	npm start
	```

#Prerequisites
1. Install [Node.js](https://docs.npmjs.com/getting-started/installing-node)
2. Install [nvm](https://github.com/creationix/nvm)
