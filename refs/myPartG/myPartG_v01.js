// Generated by Parametrix

const { polygon } = require('@jscad/modeling').primitives;
//const { subtract } = require('@jscad/modeling').booleans;
//const { union, intersect, scission, subtract } = require('@jscad/modeling').booleans;
const { union, intersect, subtract } = require('@jscad/modeling').booleans;
const { extrudeLinear, extrudeRotate } = require('@jscad/modeling').extrusions;
const { translate, rotate } = require('@jscad/modeling').transforms;

const main = () => {

const ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr000 = polygon({ points: [ [ 0.0000, 0.0000 ],
	[ 900.0000, 0.0000 ],
	[ 900.0000, 1000.0000 ],
	[ 0.0000, 1000.0000 ],
	[ 0.0000, 0.0000 ] ] });

const ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr001 = polygon({ points: [ [ 100.0000, 200.0000 ],
	[ 200.0000, 200.0000 ],
	[ 159.7014, 361.1943 ],
	[ 159.0713, 362.9774 ],
	[ 158.1167, 364.6100 ],
	[ 156.8719, 366.0337 ],
	[ 155.3812, 367.1976 ],
	[ 153.6981, 368.0600 ],
	[ 151.8827, 368.5901 ],
	[ 150.0000, 368.7689 ],
	[ 148.1173, 368.5901 ],
	[ 146.3019, 368.0600 ],
	[ 144.6188, 367.1976 ],
	[ 143.1281, 366.0337 ],
	[ 141.8833, 364.6100 ],
	[ 140.9287, 362.9774 ],
	[ 140.2986, 361.1943 ],
	[ 100.0000, 200.0000 ] ] });

const ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr002 = polygon({ points: [ [ 300.0000, 200.0000 ],
	[ 500.0000, 200.0000 ],
	[ 409.7014, 561.1943 ],
	[ 409.0713, 562.9774 ],
	[ 408.1167, 564.6100 ],
	[ 406.8719, 566.0337 ],
	[ 405.3812, 567.1976 ],
	[ 403.6981, 568.0600 ],
	[ 401.8827, 568.5901 ],
	[ 400.0000, 568.7689 ],
	[ 398.1173, 568.5901 ],
	[ 396.3019, 568.0600 ],
	[ 394.6188, 567.1976 ],
	[ 393.1281, 566.0337 ],
	[ 391.8833, 564.6100 ],
	[ 390.9287, 562.9774 ],
	[ 390.2986, 561.1943 ],
	[ 300.0000, 200.0000 ] ] });

const ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr003 = polygon({ points: [ [ 600.0000, 200.0000 ],
	[ 800.0000, 200.0000 ],
	[ 719.4029, 522.3886 ],
	[ 718.8337, 524.2677 ],
	[ 718.0831, 526.0819 ],
	[ 717.1582, 527.8138 ],
	[ 716.0680, 529.4467 ],
	[ 714.8229, 530.9648 ],
	[ 713.4350, 532.3535 ],
	[ 711.9175, 533.5994 ],
	[ 710.2853, 534.6905 ],
	[ 708.5539, 535.6164 ],
	[ 706.7400, 536.3680 ],
	[ 704.8612, 536.9381 ],
	[ 702.9356, 537.3213 ],
	[ 700.9817, 537.5138 ],
	[ 699.0183, 537.5138 ],
	[ 697.0644, 537.3213 ],
	[ 695.1388, 536.9381 ],
	[ 693.2600, 536.3680 ],
	[ 691.4461, 535.6164 ],
	[ 689.7147, 534.6905 ],
	[ 688.0825, 533.5994 ],
	[ 686.5650, 532.3535 ],
	[ 685.1771, 530.9648 ],
	[ 683.9320, 529.4467 ],
	[ 682.8418, 527.8138 ],
	[ 681.9169, 526.0819 ],
	[ 681.1663, 524.2677 ],
	[ 680.5971, 522.3886 ],
	[ 600.0000, 200.0000 ] ] });

const ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr004 = polygon({ points: [ [ 339.8638, 669.4622 ],
	[ 410.5745, 740.1729 ],
	[ 268.0975, 825.6591 ],
	[ 266.3911, 826.4744 ],
	[ 264.5617, 826.9539 ],
	[ 262.6747, 827.0803 ],
	[ 260.7977, 826.8492 ],
	[ 258.9978, 826.2689 ],
	[ 257.3392, 825.3601 ],
	[ 255.8815, 824.1552 ],
	[ 254.6767, 822.6975 ],
	[ 253.7678, 821.0390 ],
	[ 253.1875, 819.2390 ],
	[ 252.9564, 817.3620 ],
	[ 253.0829, 815.4751 ],
	[ 253.5623, 813.6456 ],
	[ 254.3776, 811.9392 ],
	[ 339.8638, 669.4622 ] ] });

const ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr005 = polygon({ points: [ [ 598.4425, 740.1729 ],
	[ 669.1532, 669.4622 ],
	[ 754.6393, 811.9392 ],
	[ 755.4547, 813.6456 ],
	[ 755.9341, 815.4751 ],
	[ 756.0606, 817.3620 ],
	[ 755.8295, 819.2390 ],
	[ 755.2492, 821.0390 ],
	[ 754.3403, 822.6975 ],
	[ 753.1355, 824.1552 ],
	[ 751.6777, 825.3601 ],
	[ 750.0192, 826.2689 ],
	[ 748.2193, 826.8492 ],
	[ 746.3423, 827.0803 ],
	[ 744.4553, 826.9539 ],
	[ 742.6259, 826.4744 ],
	[ 740.9195, 825.6591 ],
	[ 598.4425, 740.1729 ] ] });

face_fig_myPartG_faceTransforms_Fa000 = subtract( ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr000, ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr001, ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr002, ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr003, ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr004, ctr_face_fig_myPartG_faceTransforms_Fa000_Ctr005 );
fig_myPartG_faceTransforms = face_fig_myPartG_faceTransforms_Fa000;

const subpax_myPartG_tf =
	translate( [ 0, 0, 0, ],
		rotate( [ 0, 0, 0, ],
			   extrudeLinear( {height: undefined}, fig_myPartG_faceTransforms )
		)
	);

const pax_myPartG = subpax_myPartG_tf;

return pax_myPartG;
}
module.exports = { main };
