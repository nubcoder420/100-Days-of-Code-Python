from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR KEY HERE'
Bootstrap(app)

emoji_mappings = {
    'coffee': {
        '1': '☕️',
        '2': '☕️☕️',
        '3': '☕️☕️☕️',
        '4': '☕️☕️☕️☕️',
        '5': '☕️☕️☕️☕️☕️'
    },
    'wifi': {
        '1': '💪',
        '2': '💪💪',
        '3': '💪💪💪',
        '4': '💪💪💪💪',
        '5': '💪💪💪💪💪'
    },
    'power': {
        '1': '🔌',
        '2': '🔌🔌',
        '3': '🔌🔌🔌',
        '4': '🔌🔌🔌🔌',
        '5': '🔌🔌🔌🔌🔌'
    }
}

def map_rating_to_emoji(rating, rating_type):
    return emoji_mappings.get(rating_type, {}).get(rating, '')
class CafeForm(FlaskForm):

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])

    coffee_choices = [(str(i), map_rating_to_emoji(str(i), 'coffee')) for i in range(1, 6)]
    wifi_choices = [(str(i), map_rating_to_emoji(str(i), 'wifi')) for i in range(1, 6)]
    power_choices = [(str(i), map_rating_to_emoji(str(i), 'power')) for i in range(1, 6)]

    coffee_rating = SelectField('Coffee Rating', choices=coffee_choices, validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=wifi_choices, validators=[DataRequired()])
    power_outlet_rating = SelectField('Power Outlet Rating', choices=power_choices, validators=[DataRequired()])

    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():

        print('WRITING TO CSV FILE...')

        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            # In the add_cafe route
            coffee_emoji = map_rating_to_emoji(form.coffee_rating.data, 'coffee')
            wifi_emoji = map_rating_to_emoji(form.wifi_rating.data, 'wifi')
            power_emoji = map_rating_to_emoji(form.power_outlet_rating.data, 'power')

            # Write the row to the CSV file
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                form.cafe.data,
                form.location_url.data,
                form.open_time.data,
                form.closing_time.data,
                coffee_emoji,
                wifi_emoji,
                power_emoji
            ])

        print('FORM VALIDATE SUCCESS')

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
