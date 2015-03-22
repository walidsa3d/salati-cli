from pygeocoder import Geocoder
from praytimes import prayTimes
from datetime import date
import argparse
from painter import paint
import sys

class salat:

	def getcoords(self,location):
		try:
			results = Geocoder.geocode(location)
			return results[0]
		except :
			return []
	def getPrayerTimes(self,coordinates):
		timez=1
		prayers=prayTimes.getTimes(date.today(), coordinates, timez)
		return prayers
	def main(self):
		parser = argparse.ArgumentParser(usage="-h for full usage")
		parser.add_argument('city', help='Enter your city')
		args = parser.parse_args()
		data=self.getcoords(args.city)
		if not data:
			print "location doesn't exist"
			sys.exit()
		prayers=self.getPrayerTimes(data.coordinates)
		print args.city+", "+data.country+" (%s,%s)" %data.coordinates
		print paint.red("Subh:")+" "+prayers['fajr']
		print paint.blue("Dhuhr: ")+prayers['dhuhr']
		print paint.green("Asr: ")+prayers['asr']
		print paint.white("Maghreb: ")+prayers['maghrib']
		print paint.cyan("Isha: ")+prayers['isha']

if __name__ == '__main__':
	salat().main()