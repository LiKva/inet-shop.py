<!DOCTYPE html>
<html>
<head>
    <title>Interneta veikals</title>
</head>
<body>
    <h1>Interneta veikals</h1>
    <h2>Preces</h2>
    <ul>
        {% for produkts in preces %}
            <li>{{ produkts[1] }} - {{ produkts[2] }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('pievienot') }}">Pievienot preci</a>
</body>
</html>
