import os

os.environ["DB_USER"] = "tempuser"
os.environ["DB_PASS"] = "TempPass1234"
os.environ["DB_HOST"] = "127.0.0.1"
os.environ["DB_NAME"] = "tempconverter_test"
os.environ["STUDENT"] = "Ivan Tolic"
os.environ["COLLEGE"] = "Algebra Bernays University"

from app import app, db, Temperature


def test_application_with_mysql():
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False

    with app.app_context():
        Temperature.query.delete()
        db.session.commit()

    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert b"Ivan Tolic" in response.data
    assert b"Algebra Bernays University" in response.data

    response = client.post(
        "/",
        data={"celsius": "50", "submit": "Convert"},
        follow_redirects=True
    )

    assert response.status_code == 200

    with app.app_context():
        record = Temperature.query.filter_by(celsius=50).first()

        assert record is not None
        assert record.fahrenheit == 122