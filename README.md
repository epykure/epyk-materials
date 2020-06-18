
![](https://raw.githubusercontent.com/epykure/epyk-materials/master/epyk_materials/static/images/epyklogo_whole_big.png)

### Epyk with Materials UI!

An easy way to use Epyk with the Material Components extension.

Presentation
================================
This package will make a simple interface between most of the components of Materials components
and Epyk. This addon will allow you to benefit from the two world and to keep write Interactive and modern web pages from Python.

https://material-ui.com/

Compatibility
================================
epyk is compatible with the most common Web Python Frameworks (Flask and Django).
By default, the server package embeds a Flask app as it is easier to install and ready to use.

The Extension (with Epyk-UI) can be included within a Jupyter or JupyterLab project. But this will lead to some limitations - for example Ajax and Socket will not be available.

The Material extension will add extra components with a more advanced design. Those components are integrated within
the framework and all the underlying event, interactivities and styling features can be reused.

Also it is possible to mix the components and to use Epyk-UI ecosystem with Material UI.


Concept
=======

Wrapper on top of the Epyk core module to add extra freatures and shortcuts on Material web components.

Those componets are only wrapped on top of generic Epyk compnents (Epyk Composite component) and this will ensure
interaction between those components.

<div align="center" >
    <img width=200 src="https://github.com/epykure/epyk-materials/raw/master/epyk_materials/static/images/extension.PNG">
</div>

More details on those components are directly available on the [official website](https://material-ui.com/getting-started/installation/) 

This will only provide easy wrappers and automated way to add standard actions from Python.
More complex or bespoke logic might require improvements in this library.

Usage
=======

To use this extra package, it is required to import it directly. it will use Epyk core module as underlying and this
wrapper will add material entry point to the page object.

This entry point will be the one to rely on the various components.

