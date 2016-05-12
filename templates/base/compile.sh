{% extends 'base/base.sh' %}

{% block content %}
CODE_DIR=/var/code
INPUT_DIR=/var/input
OUTPUT_DIR=/var/output

{% block compile %}
{% endblock %}

RETURN=$?

if [ ${RETURN} -ne 0 ]
then
    echo ${RETURN} > ${OUTPUT_DIR}/compile_failure
    exit 1
fi

{% endblock %}