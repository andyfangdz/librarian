{% extends 'base/compile.sh' %}

{% block compile %}
g++ -std=c++11 ${CODE_DIR}/Main.cpp -o ${CODE_DIR}/Main 1>${OUTPUT_DIR}/stdout.log 2>${OUTPUT_DIR}/stderr.log
{% endblock %}
