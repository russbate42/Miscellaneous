#!/bin/sh

# art-include: main/Athena
# art-include: 23.0/Athena
# art-description: DAOD building JETM1 data22
# art-type: grid
# art-output: *.pool.root
# art-output: checkFile*.txt
# art-output: checkxAOD*.txt
# art-output: checkIndexRefs*.txt

echo ""
echo "==> Running Derivations.."
echo ""

## command line parsing
START=0
FINISH=5000

OPTSTRING=":s:f:"

while getopts ${OPTSTRING} opt; do
  case ${opt} in
    s)
      echo "Starting at --skipEvents: ${OPTARG}"
      START=$OPTARG
      ;;
    f)
      echo "Finishing at --maxEvents: ${OPTARG}"
      FINISH=$OPTARG
      ;;
    :)
      echo "Option -${OPTARG} requires an argument."
      exit 1
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      exit 1
      ;;
  esac
done

INFOTAG=_test$START-$FINISH
CURRENT_DATE_STAMP=$(date '+%Y-%m-%d')

echo ""
echo "Current date stamp: ${CURRENT_DATE_STAMP}"
echo "File info: ${INFOTAG}"
echo ""
echo "START=${START}"
echo "FINISH=${FINISH}"
echo ""

set -e

printf "Derivation_tf.py \\
--CA True \\
--inputAODFile /cvmfs/atlas-nightlies.cern.ch/repo/data/data-art/CampaignInputs/data22/AOD/data22_13p6TeV.00431906.physics_Main.merge.AOD.r13928_p5279/1000events.AOD.30220215._001367.pool.root.1 \\
--outputDAODFile art${INFOTAG}.pool.root \\
--formats JETM1 \\
--maxEvents ${START} \\
--skipEvents ${FINISH} |& tee Derivation_test_${START}-${FINISH}_${CURRENT_DATE_STAMP}.txt \n"

Derivation_tf.py \
--CA True \
--inputAODFile /cvmfs/atlas-nightlies.cern.ch/repo/data/data-art/CampaignInputs/data22/AOD/data22_13p6TeV.00431906.physics_Main.merge.AOD.r13928_p5279/1000events.AOD.30220215._001367.pool.root.1 \
--outputDAODFile art$INFOTAG.pool.root \
--formats JETM1 \
--maxEvents ${START} \
--skipEvents ${FINISH} |& tee Derivation_test_${START}-${FINISH}_${CURRENT_DATE_STAMP}.txt \n

echo "art-result: $? reco"

checkFile.py DAOD_JETM1.art$INFOTAG.pool.root > checkFile_JETM1$INFOTAG.txt

echo "art-result: $?  checkfile"

checkxAOD.py DAOD_JETM1.art$INFOTAG.pool.root > checkxAOD_JETM1$INFOTAG.txt

echo "art-result: $?  checkxAOD"

checkIndexRefs.py DAOD_JETM1.art$INFOTAG.pool.root > checkIndexRefs_JETM1$INFOTAG.txt 2>&1

echo "art-result: $?  checkIndexRefs"

