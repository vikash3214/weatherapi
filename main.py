from flask import Flask
import urllib2
import json


app = Flask(__name__)


@app.route('/')
#@app.route('/weatherapi')
def index():
    return render_template('weatherapi.html')

@app.route('/weatherapi', methods=['POST'])
def data():
	data = str(request.data)


	city=data.split("in",1)[1]
	city_n=city.replace(""""}'""",'')
	response=urllib2.urlopen('https://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&APPID=af99c48af308d22d0835469a911aef8e'%(city_n))
	html=(response.read())
	
	jsonobj=json.loads(html)
	
	s=dict(jsonobj['main'])
	for k,v in s.items():
		if k=='temp':
			temp=v
				
	
	data= {"message":"the temperature in %s is %s celcius"%(city_n,temp),"status":"ok"}
	
	
	response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
	
	return response

	



	


if __name__=="__main__":
	app.run()
