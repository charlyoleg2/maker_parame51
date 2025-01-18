#!/usr/bin/env node
// make_parts.js

import { exec } from "child_process";
import { promisify } from 'util';

// partName: fileName
const c_Parts = {
	myPartA: 'myPartA_v01',
	myPartB: 'myPartB_v01',
	myPartC: 'myPartC_v01',
	myPartD: 'myPartD_v01',
	myPartE: 'myPartE_v01',
	myPartF: 'myPartF_v01',
	myPartG: 'myPartG_v01',
	myPartH: 'myPartH_v01',
	myPartI: 'myPartI_v01',
	myPartJ: 'myPartJ_v01',
	myPartK: 'myPartK_v01',
	myPartL: 'myPartL_v01',
	myPartM: 'myPartM_v01',
	myPartN: 'myPartN_v01',
	myPartO: 'myPartO_v01',
	myPartP: 'myPartP_v01',
	myPartQ: 'myPartQ_v01',
	myPartR: 'myPartR_v01',
	myPartS: 'myPartS_v01',
	myPartT: 'myPartT_v01',
	myPartU: 'myPartU_v01',
	myPartV: 'myPartV_v01',
	myPartW: 'myPartW_v01',
};

// partName: 2D-faces
const c_svgdxf = {
	myPartA: ['faceSection', 'faceSide'],
	myPartB: ['faceFront', 'faceSide'],
	myPartC: ['faceBodyCut', 'faceBodySlant', 'faceChimneyHollow', 'faceChimney', 'faceChimneyHollow'],
	myPartD: ['faceTube1', 'faceTube2', 'faceTube1H', 'faceTube2H', 'faceTop'],
	myPartE: ['faceCartesian', 'facePolarAbs', 'facePolarRel'],
	myPartF: ['faceCorners'],
	myPartG: ['faceTransforms'],
	myPartH: ['faceCircle', 'faceLine'],
	myPartI: ['face2'],
	myPartJ: ['face1', 'face2', 'face3'],
	myPartK: ['faceSide1', 'faceSide2', 'faceTop'],
	myPartL: ['face1'],
	myPartM: ['face1'],
	myPartN: ['face1'],
	myPartO: ['face1'],
	myPartP: ['face1'],
	myPartQ: ['face1'],
	myPartR: ['faceDress', 'faceShort'],
	myPartS: ['flat', 'prf00', 'prf01', 'prf02', 'prf03', 'prf04', 'prf05', 'prf06', 'prf07', 'prf08', 'prf09'],
	myPartT: ['faceSection', 'faceSide'],
	myPartU: ['faceSide', 'faceSection'],
	myPartV: ['faceSide1', 'faceSide2', 'faceTop'],
	myPartW: ['faceTop', 'faceFace'],
};

// partName: designName
const pre51g1 = ['myPartA', 'myPartB', 'myPartC', 'myPartD'];
const pre51g2 = ['myPartE', 'myPartF', 'myPartG', 'myPartH', 'myPartI', 'myPartJ', 'myPartK'];
const pre52 = ['myPartL', 'myPartM', 'myPartN'];
const pre53 = ['myPartO', 'myPartP', 'myPartQ', 'myPartR'];
const pre53b = ['myPartS', 'myPartT', 'myPartU', 'myPartV', 'myPartW'];
function inferDesignName(partName) {
	const re = /_[A-Z][0-9]*$/;
	const desiName = partName.replace(re, '');
	let rCli = '';
	let prefix = '';
	if (pre51g1.includes(desiName)) {
		rCli = 'desi51-cli';
		prefix = 'desi51/myGroup1/';
	} else if (pre51g2.includes(desiName)) {
		rCli = 'desi51-cli';
		prefix = 'desi51/myGroup2/';
	} else if (pre52.includes(desiName)) {
		rCli = 'desi52-cli';
		prefix = 'desi52/';
	} else if (pre53.includes(desiName)) {
		rCli = 'desi53-cli';
		prefix = 'desi53/';
	} else if (pre53b.includes(desiName)) {
		rCli = 'desi53-cli';
		prefix = 'desi53b/';
	}
	if (prefix === '') {
		console.log(`err732: partName ${partName} not identified for any prefix`);
		process.exit(1);
	}
	const rDesignName = `${prefix}${desiName}`;
	return [rCli, rDesignName];
}

function getCmd(dName, fName) {
	const [cli, desiName] = inferDesignName(dName);
	console.log(`info456: reference name: ${dName}   design name: ${desiName}`);
	const rCmd = [];
	//rCmd.push('pwd');
	//rCmd.push(`ls refs/${dName}`);
	//rCmd.push(`npx ${cli} -d=${desiName} -o=refs/${dName} --outFileName=px_${fName}.json write json_param`);
	rCmd.push(`npx ${cli} -d=${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.log.txt write compute_log`);
	// svg, dxf
	for (const face of c_svgdxf[dName]) {
		rCmd.push(`npx ${cli} -d=${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}_${face}.svg write svg__${face}`);
		rCmd.push(`npx ${cli} -d=${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}_${face}.dxf write dxf__${face}`);
	}
	// paxJson
	rCmd.push(`npx ${cli} -d=${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.pax.json write pax_all`);
	// OpenSCAD
	rCmd.push(`npx ${cli} -d=${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.scad write scad_3d_openscad`);
	//rCmd.push(`openscad -o refs/${dName}/${fName}_oscad.stl refs/${dName}/${fName}.scad`);
	// JsCAD
	rCmd.push(`npx ${cli} -d=${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.js write js_3d_openjscad`);
	//rCmd.push(`cd refs && npx jscad ${dName}/${fName}.js -o ${dName}/${fName}_jscad.stl`);
	// FreeCAD
	rCmd.push(`npx ${cli} -d=${desiName} -p=refs/${dName}/px_${fName}.json -o=refs/${dName} --outFileName=${fName}.py write py_3d_freecad`);
	//rCmd.push(`freecad.cmd refs/${dName}/${fName}.py refs/${dName}/${fName}_fc`);
	//rCmd.push(`npx rimraf refs/${dName}`);
	return rCmd;
}

const aExec = promisify(exec);

async function execCmd(cmd) {
	console.log(cmd);
	try {
		const { stdout, stderr } = await aExec(cmd);
		console.log('---> stdout:');
		console.log(stdout);
		console.log('---> stderr:');
		console.log(stderr);
		console.log('---> end of log');
	} catch (err) {
		console.log(`err895: Error by executing: ${cmd}`);
		console.log(err);
		console.log(`info895: script stopped!`);
		process.exit(1);
	}
}

async function loopDesign(dList) {
	const pList = Object.keys(c_Parts);
	for (const [ idx, oneDesign ] of dList.entries()) {
		const idx2 = idx + 1;
		console.log(`${idx2} : working on ${oneDesign}`);
		if (!pList.includes(oneDesign)) {
			console.log(`err309: design ${oneDesign} is unkown!`);
			process.exit(1);
		}
		const cmds = getCmd(oneDesign, c_Parts[oneDesign]);
		for (const oneCmd of cmds) {
			await execCmd(oneCmd);
		}
		console.log(`${idx2} : end of generation of ${oneDesign}`);
	}
}

async function mhcli(args) {
	//console.log(args);
	const c_flag_all = '--all';
	const allList = Object.keys(c_Parts);
	if (args.length === 3 && args[2] === c_flag_all) {
		await loopDesign(allList);
	} else if (args.length > 2) {
		await loopDesign(args.slice(2));
	} else {
		console.log('err206: no argument provided!');
		console.log(`Possible arguments: ${c_flag_all} or the following design names:`);
		let str1 = '';
		let str2 = '';
		for (const [ idx, oneDesign ] of allList.entries()) {
			str1 += ` ${oneDesign}`;
			str2 += `${(idx + 1).toString().padStart(2, ' ')} : ${oneDesign}\n`;
		}
		console.log(str1);
		console.log(str2);
		console.log('info404: Nothing done!');
	}
}

console.log('make_parts.js says Hello!');
await mhcli(process.argv);
console.log('make_parts.js says Bye!');

