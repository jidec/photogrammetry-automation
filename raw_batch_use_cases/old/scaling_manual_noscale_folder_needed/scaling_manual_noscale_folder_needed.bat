"C:\Program Files\Capturing Reality\RealityCapture\RealityCapture.exe" -load "%~dp0scaleCO.rcproj" -align -save -newScene -addFolder "%~dp0images\noscale" -align -exportRegistration "%~dp0noscaleCO.rcalign" -newScene -load "%~dp0scaleCO.rcproj" -importComponent "%~dp0noscaleCO.rcalign" -align -setReconstructionRegionAuto -calculateNormalModel -selectLargestModelComponent -invertTrianglesSelection -removeSelectedTriangles -smooth -unwrap -calculateTexture -exportSelectedModel "%~dp0model\object_full.obj" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -simplify "%~dp0simplificationParameters.xml" -unwrap -reprojectTexture "Model 3" "Model 7" -exportSelectedModel "%~dp0model\object_reduced.obj" -save "%~dp0Project.rcproj" 





