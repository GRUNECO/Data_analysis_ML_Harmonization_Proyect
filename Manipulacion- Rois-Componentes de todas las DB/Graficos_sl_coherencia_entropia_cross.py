
import collections
import pandas as pd 
import seaborn as sns
import numpy as np
import pingouin as pg
from numpy import ceil 
import errno
from matplotlib import pyplot as plt
import os
import io
from itertools import combinations
from PIL import Image
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def graphics(data,type,path,name_band,id,id_cross=None,num_columns=4,save=True,plot=True):
    '''Function to make graphs of the given data '''
    max=data[type].max()
    sns.set(rc={'figure.figsize':(15,12)})
    sns.set_theme(style="white")
    if id=='IC':
        col='Component'
    else:
        col='ROI'
    axs=sns.catplot(x='group',y=type,data=data,hue='database',dodge=True, kind="box",col=col,col_wrap=num_columns,palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    #plt.yticks(np.arange(0,round(max),0.1))
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    if id_cross==None:
        axs.fig.suptitle(type+' in '+r'$\bf{'+name_band+r'}$'+ ' in the ICs of normalized data given by the databases')
    else:
        axs.fig.suptitle(type+' in '+id_cross+' of ' +r'$\bf{'+name_band+r'}$'+ ' in the ICs of normalized data given by the databases')

    if id=='IC':
        
        axs.add_legend(loc='upper right',bbox_to_anchor=(.59,.95),ncol=4,title="Database")
        axs.fig.subplots_adjust(top=0.85,bottom=0.121, right=0.986,left=0.05, hspace=0.138, wspace=0.062) 
        axs.fig.text(0.5, 0.04, 'Group', ha='center', va='center')
        axs.fig.text(0.01, 0.5,  type, ha='center', va='center',rotation='vertical')
    else:
        
        axs.add_legend(loc='upper right',bbox_to_anchor=(.7,.95),ncol=4,title="Database")
        axs.fig.subplots_adjust(top=0.85,bottom=0.121, right=0.986,left=0.06, hspace=0.138, wspace=0.062) # adjust the Figure in rp
        axs.fig.text(0.5, 0.04, 'Group', ha='center', va='center')
        axs.fig.text(0.015, 0.5,  type, ha='center', va='center',rotation='vertical')
    if plot:
        plt.show()
    if save==True:
        if id_cross==None:
            path_complete='{path}\Graficos_{type}\{id}\{name_band}_{type}_{id}.png'.format(path=path,name_band=name_band,id=id,type=type)  
        else:
            path_complete='{path}\Graficos_{type}\{id}\{name_band}_{id_cross}_{type}_{id}.png'.format(path=path,name_band=name_band,id=id,type=type,id_cross=id_cross)
        plt.savefig(path_complete)
    plt.close()
    return path_complete

def text_format(val,value):
    if value==0.05:
        color = 'lightgreen' if val <0.05 else 'white'
    elif value==0.8:
        if val >=0.7 and val<0.8:
            color = 'salmon'
        elif val >=0.8:
            color = 'lightblue' 
        else:
            color='white'

    return 'background-color: %s' % color

def stats_pair(data,metric,space,path,name_band,id,id_cross=None):
    from tabulate import tabulate
    from IPython.display import display
    import dataframe_image as dfi
    groups=data['group'].unique()
    combinaciones = list(combinations(groups, 2))
    test_ez={}
    test_manu={}
    for i in combinaciones:
        #Effect size
        ez=data.groupby(['database',space]).apply(lambda data:pg.compute_effsize(data[data['group']==i[0]][metric],data[data['group']==i[1]][metric])).to_frame()
        ez=ez.rename(columns={0:'effect size'})
        ez['A']=i[0]
        ez['B']=i[1]
        ez['Prueba']='effect size'
        test_ez['effsize-'+i[0]+'-'+i[1]]=ez
        #Mannwhitneyu
        manu=data.groupby(['database',space]).apply(lambda data:pg.mwu(data[data['group']==i[0]][metric],data[data['group']==i[1]][metric]))
        manu['A']=i[0]
        manu['B']=i[1]
        test_manu['Mannwhitneyu-'+i[0]+'-'+i[1]]=manu.loc[:,['U-val', 'p-val', 'A', 'B']]
        
    table_ez=pd.concat(list(test_ez.values()),axis=0)
    table_ez.reset_index( level = [0,1],inplace=True )
    table_manu=pd.concat(list(test_manu.values()),axis=0)
    table_manu.reset_index( level = [0,1,2],inplace=True )
    table_manu.rename(columns={'level_2':'Prueba'},inplace=True)
    #Gameshowell
    g=data.groupby(['database',space]).apply(lambda data:pg.pairwise_gameshowell(data,dv=metric,between='group'))
    g.reset_index( level = [0,1,2],inplace=True )
    g.drop(columns=['level_2'],inplace=True)
    g['Prueba']='Gameshowell'
    table_g=g.loc[:,[ 'database', space,'Prueba','diff','pval','A', 'B' ]]
    table_g.rename(columns={'pval':'p-val'},inplace=True)
    #Union de todas las puerbas
    table=pd.concat([table_ez,table_manu,table_g],axis=0)
    table=pd.pivot_table(table,values=['effect size','U-val','diff','p-val'],columns=['Prueba'],index=['database',space,'A', 'B'])
    table=table.T
    table=table.swaplevel(0, 1)
    table.sort_index(level=0,inplace=True)
    table=table.T
    if id_cross==None:
        path_complete='{path}\Graficos_{type}\{id}\{name_band}_{type}_{id}_table.png'.format(path=path,name_band=name_band,id=id,type=metric)  
    else:
        path_complete='{path}\Graficos_{type}\{id}\{name_band}_{id_cross}_{type}_{id}_table.png'.format(path=path,name_band=name_band,id=id,type=metric,id_cross=id_cross)
    table=table.style.applymap(text_format,value=0.05,subset=[('Gameshowell','p-val'),('MWU','p-val')]).applymap(text_format,value=0.8,subset=[('effect size', 'effect size')])
    dfi.export(table, path_complete)
    return path_complete
        
def joinimages(paths):
    import sys
    from PIL import Image
    images =[Image.open(x) for x in paths]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    new_im.save(paths[1])
    print('Done')

path=r'C:\Users\valec\OneDrive - Universidad de Antioquia\Resultados_Armonizacion_BD' #Cambia dependieron de quien lo corra

#data loading
data_p_roi=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_power_roi_without_oitliers.feather'.format(path=path))
data_p_com=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_power_components_without_oitliers.feather'.format(path=path))
data_sl_roi=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_sl_roi.feather'.format(path=path))
data_sl_com=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_sl_components.feather'.format(path=path))
data_c_roi=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_coherence_roi.feather'.format(path=path))
data_c_com=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_coherence_components.feather'.format(path=path))
data_e_roi=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_entropy_roi.feather'.format(path=path))
data_e_com=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_entropy_components.feather'.format(path=path))
data_cr_roi=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_crossfreq_roi.feather'.format(path=path))
data_cr_com=pd.read_feather(r'{path}\Datosparaorganizardataframes\data_long_crossfreq_components.feather'.format(path=path))

datos_roi={'Cross Frequency':data_cr_roi,'Power':data_p_roi,'SL':data_sl_roi,'Coherence':data_c_roi,'Entropy':data_e_roi}
datos_com={'Cross Frequency':data_cr_com,'Power':data_p_com,'SL':data_sl_com,'Coherence':data_c_com,'Entropy':data_e_com}

bands= data_sl_com['Band'].unique()
bandsm= data_cr_com['M_Band'].unique()

for band in bands:
    for metric in datos_roi.keys():
        d_roi=datos_roi[metric]
        d_banda_roi=d_roi[d_roi['Band']==band]
        d_com=datos_com[metric]
        d_banda_com=d_com[d_com['Band']==band]
        if metric!='Cross Frequency':   
            table_roi=stats_pair(d_banda_roi,metric,'ROI',path,band,'ROI')
            table_com=stats_pair(d_banda_com,metric,'Component',path,band,'IC') 
            path_roi=graphics(d_banda_roi,metric,path,band,'ROI',num_columns=2,save=True,plot=False)
            path_com=graphics(d_banda_com,metric,path,band,'IC',num_columns=4,save=True,plot=False)
            joinimages([path_roi,table_roi])
            joinimages([path_com,table_com])
        else:
            for bandm in bandsm:   
                if d_banda_roi[d_banda_roi['M_Band']==bandm]['Cross Frequency'].iloc[0]!=0:
                    table_roi=stats_pair(d_banda_roi[d_banda_roi['M_Band']==bandm],metric,'ROI',path,band,'ROI',id_cross=bandm)
                    path_roi=graphics(d_banda_roi[d_banda_roi['M_Band']==bandm],'Cross Frequency',path,band,'ROI',id_cross=bandm,num_columns=2,save=True,plot=False)
                    joinimages([path_roi,table_roi])                
                if d_banda_com[d_banda_com['M_Band']==bandm]['Cross Frequency'].iloc[0]!=0:
                    table_com=stats_pair(d_banda_com[d_banda_com['M_Band']==bandm],metric,'Component',path,band,'IC',id_cross=bandm) 
                    path_com=graphics(d_banda_com[d_banda_com['M_Band']==bandm],'Cross Frequency',path,band,'IC',id_cross=bandm,num_columns=4,save=True,plot=False)
                    joinimages([path_com,table_com])
print('Graficos SL,coherencia,entropia y cross frequency guardados')