# Data_analysis_ML_Harmonization_Proyect

Orden de archivos:

1. ProcessingEEG.py 
2. Dataframes_potencias_Componentes_Demograficos.py 
3. Borrar_datos_atipicos_potencias.py 
4. Dataframes_SL_Coherencia_Entropy_Cross.py 
5. neuroharmonaze_G1CTR.py 
6. unirfeatherharmonize.py 
7. Graficos_power_sl_coherencia_entropia_cross.py
8. graficos_data_harmonized.py
9. ML_models_G1_ic_sovaharmony.py * Mirar notas
10. ML_models_G1_ic_neuroHarmonize.py * Mirar notas

NOTAS
* Los pasos 7,8,9 y 10 pueden ejecutarse simultáneamente sin necesidad de esperar los resultados de los pasos anteriores
* El código de ML integrado y optimizado se encuentra en el script: training_script.py y utiliza las funciones de training_functions.py

# Archivos adicionales para papers = (2 ICA - 54x10 y 58x25) y (Diversificación de dataset 2to1, 5to1 y 10to1)

1. neuroharmonize - V2.py => Se necesita el archivo "Data_complete_ic.feather". Repositirorio eeg_harmonization
2. unirfeatherharmonize - V2.py => Se necesita la ruta de la carpeta "complete" que contiene los complete para cada metrica. Repositorio Data_analysis_ML_Harmonization_Proyect
3. training_script3.py => Se necesita la ruta de la carpeta "integrate" que contiene los integrate para cada metrica. Repositorio Data_analysis_ML_Harmonization_Proyect

# Archivos adicionales de graficos de interes (independientes de los todos los scripts

1. Topofeatures.py edificion del codigo original topo.py del repositorio eeg_harmonization
2. Graficos_Paper.py => Se ejecuta drante el debbug de (3.) para graficar y analizar los resultados por medio de graficas. 


## Refereed article
### 1.	Refereed article
*Title of article:* 	Longitudinal test-retest reliability of quantitative EEG in healthy individuals using an automated preprocessing approach.<br>
*Author(s):* 	Henao Isaza V, Cadavid Castro V, Zapata-Saldarriaga LM, Mantilla-Ramos YJ, Suarez-Revelo JX, Tobón-Quintero CA, Ochoa-Gómez JF.<br>
*Title of publication:* 	Biomedical Signal Processing and Control<br>
*ISSN:* 	1746-8094<br>
*Volume/Issue and page number:* 	Volume 116, Article 109484<br>
*Date of publication or accepted for publication:* 	2026<br>
*Peer review proof:* 	Peer-reviewed journal, indexed in the Scopus database<br>
*Scopus Author ID:* 58685767300<br>

### 2.	Refereed article
*Title of article:* 	Tackling EEG Test-Retest Reliability with a Pre-Processing Pipeline based on ICA and Wavelet-ICA.<br>
*Author(s):* 	Henao Isaza V, Cadavid Castro V, Zapata Saldarriaga L, Mantilla-Ramos Y, Tobón Quintero C, Suarez Revelo J, Ochoa Gómez J.<br>
*Title of publication:* 	Authorea Preprints<br>
*ISSN:* 	Pre-print<br>
*Volume/Issue and page number:* 	Pre-print<br>
*Date of publication or accepted for publication:* 	June 2023<br>
*Peer review proof:* 	Listed on the Scopus database<br>
*Scopus Author ID:* 58685767300<br>

*URL to article:* 	https://doi.org/10.22541/au.168570191.12788016/v1<br>

### 3.	Refereed article
*Title of article:* 	Longitudinal Analysis of qEEG in Subjects with Autosomal Dominant Alzheimer's Disease due to PSEN1-E280A Variant.<br>
*Author(s):* 	Aguillon, D., Guerrero, A., Vasquez, D., Cadavid, V., Henao, V., Suarez, X., ... & Ochoa, J. F.<br>
*Title of publication:* 	Alzheimer's Association International Conference. ALZ.<br>
*ISSN:* 	NA<br>
*Volume/Issue and page number:* 	NA<br>
*Date of publication or accepted for publication:* 	December 2023<br>
*Peer review proof:* 	NA<br>
*URL to article:* 	https://alz-journals.onlinelibrary.wiley.com/doi/abs/10.1002/alz.083226<br>

### 4.	Refereed article
*Title of article:* 	Spectral features of resting-state EEG in Parkinson's Disease: a multicenter study using functional data analysis<br>
*Author(s):* 	Alberto Jaramillo-Jimenez, Diego A Tovar-Rios, Johann Alexis Ospina, Yorguin-Jose Mantilla-Ramos, Daniel Loaiza-López, Verónica Henao Isaza, Luisa María Zapata Saldarriaga, Valeria Cadavid Castro, Jazmin Ximena Suarez-Revelo, Yamile Bocanegra, Francisco Lopera, David Antonio Pineda-Salazar, Carlos Andrés Tobón Quintero, John Fredy Ochoa-Gomez, Miguel Germán Borda, Dag Aarsland, Laura Bonanni, Kolbjørn Brønnick<br>
*Title of publication:* 	Clinical Neurophysiology<br>
*ISSN:* 	1388-2457<br>
*Volume/Issue and page number:* 	Volume 151, July 2023, Pages 28-40<br>
*Date of publication or accepted for publication:* 	April 2023<br>
*Peer review proof:* 	Listed on the Scopus database<br>
*Scopus Author ID:* 58685767300<br>

*URL to article:* 	https://www.sciencedirect.com/science/article/pii/S1388245723005989<br>

### 5.	Refereed article
*Title of article:* 	Comprehensive methodology for sample enrichment in EEG biomarker studies for Alzheimer's risk classification.<br>
*Author(s):* 	Henao Isaza V, Aguillon D, Tobón-Quintero CA, Lopera F, Ochoa-Gómez JF.<br>
*Title of publication:* 	PLOS One<br>
*ISSN:* 	1932-6203<br>
*Volume/Issue and page number:* 	Volume 21, Issue 3, e0343722<br>
*Date of publication or accepted for publication:* 	March 2026<br>
*Peer review proof:* 	Peer-reviewed journal<br>
*URL to article:* 	https://doi.org/10.1371/journal.pone.0343722<br>

