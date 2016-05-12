#!/usr/bin/env bash

{% block header %}
{% endblock %}

{% block content %}
{% endblock %}

# trap SIGINT, SIGTERM and SIGEXIT to enable fast shutdown of docker image
trap "exit $?" INT TERM EXIT