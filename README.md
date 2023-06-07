# Titanic - Machine Learning from Disaster

This repo contains code that implemtents the [Kaggle Titanic challenge](https://www.kaggle.com/competitions/titanic/) through two new packages for the [BRANE framework](https://wiki.enablingpersonalizedinterventions.nl/user-guide/welcome.html). 

## Build

When BRANE is correctly set up, each package can be individually imported with the following command:

```bash
brane import robertvanstraten/wscbs4b -c packages/<PACKAGE_NAME>/container.yml
```

However, one can also clone this repository and navigate to the folder of a package and run the following command to build the package:

```
brane build container.yml
```

## Attribution

This project was heavily inspired by the [Natural Language Processing with Disaster Tweets GitHub repo](https://github.com/epi-project/brane-disaster-tweets-example) for understanding how to deal with Brane and the challenge approach is exactly as described in [Alexis Cook's tutorial](https://www.kaggle.com/code/alexisbcook/titanic-tutorial/notebook) on the Kaggle Titanic challenge.
