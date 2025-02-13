// Generated by Parametrix

const { polygon } = require('@jscad/modeling').primitives;
//const { subtract } = require('@jscad/modeling').booleans;
//const { union, intersect, scission, subtract } = require('@jscad/modeling').booleans;
const { union, intersect, subtract } = require('@jscad/modeling').booleans;
const { extrudeLinear, extrudeRotate } = require('@jscad/modeling').extrusions;
const { translate, rotate } = require('@jscad/modeling').transforms;

const main = () => {

const ctr_face_fig_myPartI_face2_Fa000_Ctr000 = polygon({ points: [ [ 0.0000, -0.0000 ],
	[ 180.0000, 0.0000 ],
	[ 180.0000, 70.0000 ],
	[ 179.8079, 71.9509 ],
	[ 179.2388, 73.8268 ],
	[ 178.3147, 75.5557 ],
	[ 177.0711, 77.0711 ],
	[ 175.5557, 78.3147 ],
	[ 173.8268, 79.2388 ],
	[ 171.9509, 79.8079 ],
	[ 170.0000, 80.0000 ],
	[ 0.0000, 80.0000 ],
	[ 0.0000, -0.0000 ] ] });

const ctr_face_fig_myPartI_face2_Fa000_Ctr001 = polygon({ points: [ [ 30.0000, 20.0000 ],
	[ 60.0000, 20.0000 ],
	[ 45.0000, 60.0000 ],
	[ 30.0000, 20.0000 ] ] });

const ctr_face_fig_myPartI_face2_Fa000_Ctr002 = polygon({ points: [ [ 105.0000, 60.0000 ],
	[ 75.0000, 60.0000 ],
	[ 90.0000, 20.0000 ],
	[ 105.0000, 60.0000 ] ] });

const ctr_face_fig_myPartI_face2_Fa000_Ctr003 = polygon({ points: [ [ 120.0000, 20.0000 ],
	[ 150.0000, 20.0000 ],
	[ 135.0000, 60.0000 ],
	[ 120.0000, 20.0000 ] ] });

face_fig_myPartI_face2_Fa000 = subtract( ctr_face_fig_myPartI_face2_Fa000_Ctr000, ctr_face_fig_myPartI_face2_Fa000_Ctr001, ctr_face_fig_myPartI_face2_Fa000_Ctr002, ctr_face_fig_myPartI_face2_Fa000_Ctr003 );
fig_myPartI_face2 = face_fig_myPartI_face2_Fa000;

const subpax_myPartI_2 =
	translate( [ 0, 0, 0, ],
		rotate( [ 0, 0, 0, ],
			   extrudeLinear( {height: 1}, fig_myPartI_face2 )
		)
	);

const pax_myPartI = subpax_myPartI_2;

return pax_myPartI;
}
module.exports = { main };
