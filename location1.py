from flask import Flask, render_template, request
import ipinfo

app = Flask(__name__, template_folder='C:\\Users\\ANUSH\\OneDrive\\Desktop\\location1\\template')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/location', methods=['POST'])
def get_location():
    ip_addresses = request.form['ip_addresses'].strip().split(',')[:5]  # Split input into a list of up to 5 IP addresses
    access_token = 'YOUR_IPINFO_ACCESS_TOKEN'
    handler = ipinfo.getHandler(access_token)

    ip_details = []
    for ip_address in ip_addresses:
        details = handler.getDetails(ip_address.strip())
        city = details.city or 'Unknown'
        region = details.region or 'Unknown'
        country = details.country or 'Unknown'
        ip_details.append(f'IP Address: {ip_address}, City: {city}, Region: {region}, Country: {country}')

    return '<br>'.join(ip_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
