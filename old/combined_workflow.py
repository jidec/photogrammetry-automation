from old.pg_auto import setScaleMarkersAuto
from old.pg_auto import setScaleDistanceManual
from old.pg_auto import setScaleFinalAuto
from old.pg_auto import createModelAuto

specimens = ["2022_7", "UF_IZ_312313", "UF_IZ_312313", "UF_IZ_312313"]
specimens = ["2022_7/UF_IZ_312313","2022_4/XYZ"]

setScaleMarkersAuto(specimens)

setScaleDistanceManual(specimens)

setScaleFinalAuto(specimens)
createModelAuto(specimens)


