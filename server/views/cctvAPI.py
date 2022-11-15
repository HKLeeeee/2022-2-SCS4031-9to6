from flask import jsonify
from flask_restful import Resource
from model import db
from model.cctv import CCTV, CCTVSchema

class CCTVS(Resource):
	def get(self, cctv_id):
		cctv = db.one_or_404(db.select(CCTV).filter_by(ID=cctv_id))
		cctv_schema = CCTVSchema()
		output = cctv_schema.dump(cctv)
		return jsonify({'cctv' : output})

class CCTVList(Resource):
	def get(self):
		cctvs = CCTV.query.all()
		cctv_schema = CCTVSchema(many=True)
		output = cctv_schema.dump(cctvs)
		return jsonify({'cctv' : output})