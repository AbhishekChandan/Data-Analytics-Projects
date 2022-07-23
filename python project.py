
import pandas as pd
data=pd.read_csv("Weather Data.csv")
data

'''1/1/2012 0:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	1/1/2012 1:00	-1.8	-3.7	87	4	8.0	101.24	Fog
2	1/1/2012 2:00	-1.8	-3.4	89	7	4.0	101.26	Freezing Drizzle,Fog
3	1/1/2012 3:00	-1.5	-3.2	88	6	4.0	101.27	Freezing Drizzle,Fog
4	1/1/2012 4:00	-1.5	-3.3	88	7	4.8	101.23	Fog
...	...	...	...	...	...	...	...	...
8779	12/31/2012 19:00	0.1	-2.7	81	30	9.7	100.13	Snow
8780	12/31/2012 20:00	0.2	-2.4	83	24	9.7	100.03	Snow
8781	12/31/2012 21:00	-0.5	-1.5	93	28	4.8	99.95	Snow
8782	12/31/2012 22:00	-0.2	-1.8	89	28	9.7	99.91	Snow
8783	12/31/2012 23:00	0.0	-2.1	86	30	11.3	99.89	Snow
8784 rows × 8 columns'''

data.dtypes

'''Date/Time            object
Temp_C              float64
Dew Point Temp_C    float64
Rel Hum_%             int64
Wind Speed_km/h       int64
Visibility_km       float64
Press_kPa           float64
Weather              object
dtype: object'''

data.columns

'''Index(['Date/Time', 'Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
       'Wind Speed_km/h', 'Visibility_km', 'Press_kPa', 'Weather'],
      dtype='object')'''


data['Weather'].unique()

'''array(['Fog', 'Freezing Drizzle,Fog', 'Mostly Cloudy', 'Cloudy', 'Rain',
       'Rain Showers', 'Mainly Clear', 'Snow Showers', 'Snow', 'Clear',
       'Freezing Rain,Fog', 'Freezing Rain', 'Freezing Drizzle',
       'Rain,Snow', 'Moderate Snow', 'Freezing Drizzle,Snow',
       'Freezing Rain,Snow Grains', 'Snow,Blowing Snow', 'Freezing Fog',
       'Haze', 'Rain,Fog', 'Drizzle,Fog', 'Drizzle',
       'Freezing Drizzle,Haze', 'Freezing Rain,Haze', 'Snow,Haze',
       'Snow,Fog', 'Snow,Ice Pellets', 'Rain,Haze', 'Thunderstorms,Rain',
       'Thunderstorms,Rain Showers', 'Thunderstorms,Heavy Rain Showers',
       'Thunderstorms,Rain Showers,Fog', 'Thunderstorms',
       'Thunderstorms,Rain,Fog',
       'Thunderstorms,Moderate Rain Showers,Fog', 'Rain Showers,Fog',
       'Rain Showers,Snow Showers', 'Snow Pellets', 'Rain,Snow,Fog',
       'Moderate Rain,Fog', 'Freezing Rain,Ice Pellets,Fog',
       'Drizzle,Ice Pellets,Fog', 'Drizzle,Snow', 'Rain,Ice Pellets',
       'Drizzle,Snow,Fog', 'Rain,Snow Grains', 'Rain,Snow,Ice Pellets',
       'Snow Showers,Fog', 'Moderate Snow,Blowing Snow'], dtype=object)'''


data.nunique()
'''Date/Time           8784
Temp_C               533
Dew Point Temp_C     489
Rel Hum_%             83
Wind Speed_km/h       34
Visibility_km         24
Press_kPa            518
Weather               50
dtype: int64'''

data['Temp_C'].nunique()

'''533'''

data['Temp_C'].unique()


'''array([ -1.8,  -1.5,  -1.4,  -1.3,  -1. ,  -0.5,  -0.2,   0.2,   0.8,
         1.8,   2.6,   3. ,   3.8,   3.1,   3.2,   4. ,   4.4,   5.3,
         5.2,   4.6,   3.9,   3.7,   2.9,   2.3,   2. ,   1.9,   1.5,
         2.2,   1.7,   1.1,   0. ,  -0.7,  -2.1,  -4.1,  -4.8,  -5.6,
        -5.8,  -7. ,  -7.4,  -9. ,  -9.7, -10.5, -11.3, -12.6, -12.9,
       -13.3, -14. , -14.8, -15. , -15.3, -14.9, -15.1, -15.8, -16.3,
       -16.9, -17.3, -17. , -17.1, -17.5, -17.9, -18.1, -18.5, -18.6,
       -18.2, -17.8, -16.8, -15.2, -14.2, -13.7, -12.4, -10.2,  -9.4,
        -8.9,  -8.4,  -7.8,  -7.6,  -9.5,  -9.6,  -8.8,  -7.5,  -5.4,
        -5. ,  -8.2,  -7.1,  -6.1,  -6.6,  -6. ,  -4.7,  -4.4,  -5.1,
        -4.3,  -6.7,  -9.2,  -9.8,  -9.9, -10. , -10.6, -11.8, -12. ,
       -14.4, -12.3, -12.5, -11.7, -11.9, -11.2, -11.5, -11.6,  -9.3,
        -8.7,  -8.5,  -8.1,  -6.9,  -6.4,  -5.7,  -5.5,  -3.7,  -3.6,
        -3.1,  -3.2,  -3. ,   0.4,   0.6,  -0.6,  -1.7,  -3.5,  -5.9,
        -6.5,  -7.2,  -8. ,  -8.3,  -7.7,  -6.8,  -2.5,  -1.1,  -0.3,
         2.5,   1.4,   1.6,   1.2,   0.7,  -4. ,  -4.9,  -7.3,  -8.6,
       -10.7, -12.7, -13.4, -13.9, -14.7, -14.3, -12.2, -11.4, -10.8,
        -6.2,  -5.2,  -4.6,  -4.5,  -2.9, -18. , -16.7, -17.4, -17.7,
       -18.3, -19.6, -20. , -19.9, -20.3, -21.2, -21.1, -21.4, -20.7,
       -21. , -21.3, -23.2, -22.8, -23.3, -22.2, -20.6, -19.3, -16. ,
       -15.4, -16.2, -19.2, -18.7, -19.1, -13.6, -10.1, -10.4,  -5.3,
        -3.3,  -1.6,   2.1,   0.5, -10.9, -11.1, -11. , -10.3, -16.6,
       -14.6,  -4.2,  -3.9,  -6.3, -15.5, -15.9, -16.4, -16.1, -12.1,
       -13. , -17.6, -18.4, -17.2, -19.5, -19. , -14.5, -13.2,   2.7,
         3.3,   3.6,   3.5,   5. ,   4.2,   3.4,   2.8,   2.4,   1.3,
         1. ,  -0.1,  -0.4,  -2.8,  -7.9,  -3.4,  -3.8,  -0.8,   0.3,
         0.1,  -1.2,   0.9,  -0.9,  -2. ,  -1.9,  -2.2,  -2.3, -15.7,
       -13.5, -13.8,  -2.4, -13.1, -12.8,  -2.7,   5.8,   6.1,   5.4,
         6.5,   4.3,   6.4,   8.9,   9.3,   9.7,  11.4,   9.9,   5.5,
         6. ,   7.6,   6.8,   4.8,   6.2,   7.9,  10.1,  10. ,   5.7,
        10.3,   6.7,  10.2,  12.1,  12.7,  11.7,  11.5,  11.6,  11.3,
        10.5,  -2.6,   5.9,   9. ,   9.5,  10.9,  10.7,   9.1,   7.4,
         8.3,  10.6,  10.8,  12.3,  12.4,  11.8,   8.7,   9.2,   8.4,
         6.6,   7.5,   5.1,   4.9,   4.1,   8.1,   9.8,   8.8,   7.7,
        10.4,  11.9,  14.1,  17.3,  20. ,  21.7,  22.2,  22.7,  21.8,
        18.4,  17.1,  12.8,  13.4,  12.6,  11.2,  13.9,  15.6,  17.8,
        19.8,  18.5,  17. ,  16.3,  16.6,  15.9,  12.5,   7.2,   7.1,
         8. ,  14.9,  16.5,  21.5,  22.5,  23.3,  22. ,  19.7,  17.5,
        18.1,  16. ,  14.2,  14.3,  14. ,  13.8,  18.2,  20.2,  22.3,
        23.8,  24.7,  25.4,  25.5,  25.2,  20.7,  17.2,  16.4,  18. ,
        15.5,  15. ,  11. ,  13.2,  13.7,  15.4,  19.6,  20.4,  23. ,
        22.8,  21.4,  16.7,  15.1,  14.5,  16.2,  16.8,  14.7,   7.3,
         4.7,   6.3,   4.5,   8.2,   7. ,   6.9,   7.8,   5.6,   8.5,
         8.6,   9.4,  12.2,  13.5,  16.1,  13.6,  15.3,  14.8,  12. ,
        12.9,  13.1,  19.4,  14.6,  15.7,  14.4,  15.2,  19.3,  24.9,
        24.1,  24.8,  26.6,  27.4,  27.8,  27.3,  26.7,  26.4,  20.5,
        19.5,  19. ,  18.9,  17.4,  11.1,  15.8,  18.7,   9.6,  13. ,
        13.3,  16.9,  20.1,  20.6,  20.9,  21. ,  19.9,  19.2,  17.6,
        17.9,  18.6,  22.4,  23.9,  23.6,  18.8,  21.2,  21.9,  23.2,
        23.4,  23.5,  22.9,  18.3,  20.3,  20.8,  17.7,  19.1,  25.6,
        25.8,  26. ,  24.3,  21.6,  26.8,  28.6,  29.5,  30.9,  31.2,
        30.8,  29.2,  26.9,  25.9,  24. ,  28. ,  28.4,  28.8,  28.9,
        28.2,  27.7,  26.5,  21.1,  24.6,  26.1,  27.1,  27.6,  28.1,
        24.4,  23.1,  27.2,  26.2,  21.3,  22.1,  22.6,  24.2,  23.7,
        25.3,  28.7,  29.4,  30.1,  29.6,  29.1,  25. ,  24.5,  25.7,
        27. ,  27.9,  26.3,  28.5,  29.7,  31.7,  32.2,  32.3,  32.4,
        30.6,  25.1,  31.8,  31.6,  32.6,  33. ,  32.5,  32.1,  31.1,
        30.3,  27.5,  29. ,  29.8,  30.7,  30.2,  29.9,  28.3,  30.5,
        30.4,  31.9,  31.4,  32.7,  32.9,  31.5,  29.3,  30. ,  32. ,
        32.8,  -9.1])'''



data.count()
'''Date/Time           8784
Temp_C              8784
Dew Point Temp_C    8784
Rel Hum_%           8784
Wind Speed_km/h     8784
Visibility_km       8784
Press_kPa           8784
Weather             8784
dtype: int64'''

data['Weather'].value_counts()

'''Mainly Clear                               2106
Mostly Cloudy                              2069
Cloudy                                     1728
Clear                                      1326
Snow                                        390
Rain                                        306
Rain Showers                                188
Fog                                         150
Rain,Fog                                    116
Drizzle,Fog                                  80
Snow Showers                                 60
Drizzle                                      41
Snow,Fog                                     37
Snow,Blowing Snow                            19
Rain,Snow                                    18
Haze                                         16
Thunderstorms,Rain Showers                   16
Drizzle,Snow,Fog                             15
Freezing Rain                                14
Freezing Drizzle,Snow                        11
Freezing Drizzle                              7
Snow,Ice Pellets                              6
Freezing Drizzle,Fog                          6
Snow,Haze                                     5
Freezing Rain,Fog                             4
Moderate Snow                                 4
Snow Showers,Fog                              4
Freezing Fog                                  4
Rain,Snow,Ice Pellets                         4
Thunderstorms,Rain                            3
Freezing Drizzle,Haze                         3
Rain,Haze                                     3
Thunderstorms,Rain Showers,Fog                3
Rain Showers,Snow Showers                     2
Moderate Snow,Blowing Snow                    2
Freezing Rain,Haze                            2
Thunderstorms                                 2
Drizzle,Snow                                  2
Moderate Rain,Fog                             1
Rain,Snow,Fog                                 1
Thunderstorms,Rain,Fog                        1
Drizzle,Ice Pellets,Fog                       1
Snow Pellets                                  1
Freezing Rain,Ice Pellets,Fog                 1
Rain,Ice Pellets                              1
Rain,Snow Grains                              1
Thunderstorms,Moderate Rain Showers,Fog       1
Freezing Rain,Snow Grains                     1
Thunderstorms,Heavy Rain Showers              1
Rain Showers,Fog                              1
Name: Weather, dtype: int64'''

data['Weather'].unique()
'''array(['Fog', 'Freezing Drizzle,Fog', 'Mostly Cloudy', 'Cloudy', 'Rain',
       'Rain Showers', 'Mainly Clear', 'Snow Showers', 'Snow', 'Clear',
       'Freezing Rain,Fog', 'Freezing Rain', 'Freezing Drizzle',
       'Rain,Snow', 'Moderate Snow', 'Freezing Drizzle,Snow',
       'Freezing Rain,Snow Grains', 'Snow,Blowing Snow', 'Freezing Fog',
       'Haze', 'Rain,Fog', 'Drizzle,Fog', 'Drizzle',
       'Freezing Drizzle,Haze', 'Freezing Rain,Haze', 'Snow,Haze',
       'Snow,Fog', 'Snow,Ice Pellets', 'Rain,Haze', 'Thunderstorms,Rain',
       'Thunderstorms,Rain Showers', 'Thunderstorms,Heavy Rain Showers',
       'Thunderstorms,Rain Showers,Fog', 'Thunderstorms',
       'Thunderstorms,Rain,Fog',
       'Thunderstorms,Moderate Rain Showers,Fog', 'Rain Showers,Fog',
       'Rain Showers,Snow Showers', 'Snow Pellets', 'Rain,Snow,Fog',
       'Moderate Rain,Fog', 'Freezing Rain,Ice Pellets,Fog',
       'Drizzle,Ice Pellets,Fog', 'Drizzle,Snow', 'Rain,Ice Pellets',
       'Drizzle,Snow,Fog', 'Rain,Snow Grains', 'Rain,Snow,Ice Pellets',
       'Snow Showers,Fog', 'Moderate Snow,Blowing Snow'], dtype=object)'''

data[data['Weather']=='Cloudy']

'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
17	1/1/2012 17:00	3.0	0.0	81	13	16.1	99.81	Cloudy
20	1/1/2012 20:00	3.2	1.3	87	19	25.0	99.50	Cloudy
21	1/1/2012 21:00	4.0	1.7	85	20	25.0	99.39	Cloudy
23	1/1/2012 23:00	5.3	2.0	79	30	25.0	99.31	Cloudy
25	1/2/2012 1:00	4.6	0.0	72	39	25.0	99.26	Cloudy
...	...	...	...	...	...	...	...	...
8761	12/31/2012 1:00	-10.7	-14.0	77	15	25.0	101.50	Cloudy
8762	12/31/2012 2:00	-10.1	-13.4	77	9	25.0	101.45	Cloudy
8764	12/31/2012 4:00	-10.5	-12.8	83	11	25.0	101.34	Cloudy
8765	12/31/2012 5:00	-10.2	-12.4	84	6	25.0	101.28	Cloudy
8766	12/31/2012 6:00	-9.7	-11.7	85	4	25.0	101.23	Cloudy
1728 rows × 8 columns'''


data[data["Weather"].str.contains("Snow")]

'''	Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
41	1/2/2012 17:00	-2.1	-9.5	57	22	25.0	99.66	Snow Showers
44	1/2/2012 20:00	-5.6	-13.4	54	24	25.0	100.07	Snow Showers
45	1/2/2012 21:00	-5.8	-12.8	58	26	25.0	100.15	Snow Showers
47	1/2/2012 23:00	-7.4	-14.1	59	17	19.3	100.27	Snow Showers
48	1/3/2012 0:00	-9.0	-16.0	57	28	25.0	100.35	Snow Showers
...	...	...	...	...	...	...	...	...
8779	12/31/2012 19:00	0.1	-2.7	81	30	9.7	100.13	Snow
8780	12/31/2012 20:00	0.2	-2.4	83	24	9.7	100.03	Snow
8781	12/31/2012 21:00	-0.5	-1.5	93	28	4.8	99.95	Snow
8782	12/31/2012 22:00	-0.2	-1.8	89	28	9.7	99.91	Snow
8783	12/31/2012 23:00	0.0	-2.1	86	30	11.3	99.89	Snow
583 rows × 8 columns'''


data.info()
'''<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8784 entries, 0 to 8783
Data columns (total 8 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Date/Time         8784 non-null   object 
 1   Temp_C            8784 non-null   float64
 2   Dew Point Temp_C  8784 non-null   float64
 3   Rel Hum_%         8784 non-null   int64  
 4   Wind Speed_km/h   8784 non-null   int64  
 5   Visibility_km     8784 non-null   float64
 6   Press_kPa         8784 non-null   float64
 7   Weather           8784 non-null   object 
dtypes: float64(4), int64(2), object(2)
memory usage: 549.1+ KB'''


data["Wind Speed_km/h"].value_counts()

'''9     830
11    791
13    735
15    719
7     677
17    666
19    616
6     609
20    496
4     474
22    439
24    374
0     309
26    242
28    205
30    161
32    139
33     85
35     53
37     45
39     24
41     22
44     14
43     13
48     13
46     11
52      7
57      5
50      4
2       2
63      1
54      1
70      1
83      1
Name: Wind Speed_km/h, dtype: int64'''

data[data["Weather"]=="Clear"]

'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
67	1/3/2012 19:00	-16.9	-24.8	50	24	25.0	101.74	Clear
114	1/5/2012 18:00	-7.1	-14.4	56	11	25.0	100.71	Clear
115	1/5/2012 19:00	-9.2	-15.4	61	7	25.0	100.80	Clear
116	1/5/2012 20:00	-9.8	-15.7	62	9	25.0	100.83	Clear
117	1/5/2012 21:00	-9.0	-14.8	63	13	25.0	100.83	Clear
...	...	...	...	...	...	...	...	...
8646	12/26/2012 6:00	-13.4	-14.8	89	4	25.0	102.47	Clear
8698	12/28/2012 10:00	-6.1	-8.6	82	19	24.1	101.27	Clear
8713	12/29/2012 1:00	-11.9	-13.6	87	11	25.0	101.31	Clear
8714	12/29/2012 2:00	-11.8	-13.1	90	13	25.0	101.33	Clear
8756	12/30/2012 20:00	-13.8	-16.5	80	24	25.0	101.52	Clear
1326 rows × 8 columns'''


data.groupby('Weather').get_group('Clear')

'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
67	1/3/2012 19:00	-16.9	-24.8	50	24	25.0	101.74	Clear
114	1/5/2012 18:00	-7.1	-14.4	56	11	25.0	100.71	Clear
115	1/5/2012 19:00	-9.2	-15.4	61	7	25.0	100.80	Clear
116	1/5/2012 20:00	-9.8	-15.7	62	9	25.0	100.83	Clear
117	1/5/2012 21:00	-9.0	-14.8	63	13	25.0	100.83	Clear
...	...	...	...	...	...	...	...	...
8646	12/26/2012 6:00	-13.4	-14.8	89	4	25.0	102.47	Clear
8698	12/28/2012 10:00	-6.1	-8.6	82	19	24.1	101.27	Clear
8713	12/29/2012 1:00	-11.9	-13.6	87	11	25.0	101.31	Clear
8714	12/29/2012 2:00	-11.8	-13.1	90	13	25.0	101.33	Clear
8756	12/30/2012 20:00	-13.8	-16.5	80	24	25.0	101.52	Clear
1326 rows × 8 columns'''

data.columns

'''Index(['Date/Time', 'Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
       'Wind Speed_km/h', 'Visibility_km', 'Press_kPa', 'Weather'],
      dtype='object')'''


data[data["Wind Speed_km/h"]==4]

'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	1/1/2012 0:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	1/1/2012 1:00	-1.8	-3.7	87	4	8.0	101.24	Fog
96	1/5/2012 0:00	-8.8	-11.7	79	4	9.7	100.32	Snow
101	1/5/2012 5:00	-7.0	-9.5	82	4	4.0	100.19	Snow
146	1/7/2012 2:00	-8.1	-11.1	79	4	19.3	100.15	Cloudy
...	...	...	...	...	...	...	...	...
8768	12/31/2012 8:00	-8.6	-10.3	87	4	3.2	101.14	Snow Showers
8769	12/31/2012 9:00	-8.1	-9.6	89	4	2.4	101.09	Snow
8770	12/31/2012 10:00	-7.4	-8.9	89	4	6.4	101.05	Snow,Fog
8772	12/31/2012 12:00	-5.8	-7.5	88	4	12.9	100.78	Snow
8773	12/31/2012 13:00	-4.6	-6.6	86	4	12.9	100.63	Snow
474 rows × 8 columns'''

data.isnull().sum()

'''Date/Time           0
Temp_C              0
Dew Point Temp_C    0
Rel Hum_%           0
Wind Speed_km/h     0
Visibility_km       0
Press_kPa           0
Weather             0
dtype: int64'''

data.notnull().sum()

'''Date/Time           8784
Temp_C              8784
Dew Point Temp_C    8784
Rel Hum_%           8784
Wind Speed_km/h     8784
Visibility_km       8784
Press_kPa           8784
Weather             8784
dtype: int64'''


data.rename(columns={"Weather":"Weather Condiion"},inplace=True)
'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather Condiion
0	1/1/2012 0:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	1/1/2012 1:00	-1.8	-3.7	87	4	8.0	101.24	Fog
2	1/1/2012 2:00	-1.8	-3.4	89	7	4.0	101.26	Freezing Drizzle,Fog
3	1/1/2012 3:00	-1.5	-3.2	88	6	4.0	101.27	Freezing Drizzle,Fog
4	1/1/2012 4:00	-1.5	-3.3	88	7	4.8	101.23	Fog
...	...	...	...	...	...	...	...	...
8779	12/31/2012 19:00	0.1	-2.7	81	30	9.7	100.13	Snow
8780	12/31/2012 20:00	0.2	-2.4	83	24	9.7	100.03	Snow
8781	12/31/2012 21:00	-0.5	-1.5	93	28	4.8	99.95	Snow
8782	12/31/2012 22:00	-0.2	-1.8	89	28	9.7	99.91	Snow
8783	12/31/2012 23:00	0.0	-2.1	86	30	11.3	99.89	Snow
8784 rows × 8 columns'''

data.Visibility_km.mean()

'''27.66444672131151'''

data["Press_kPa"].std()

'''0.8440047459486474'''


data["Rel Hum_%"].var()

'''286.2485501984998'''


data[(data["Wind Speed_km/h"]>24) & (data['Visibility_km']==25)]

'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
23	1/1/2012 23:00	5.3	2.0	79	30	25.0	99.31	Cloudy
24	1/2/2012 0:00	5.2	1.5	77	35	25.0	99.26	Rain Showers
25	1/2/2012 1:00	4.6	0.0	72	39	25.0	99.26	Cloudy
26	1/2/2012 2:00	3.9	-0.9	71	32	25.0	99.26	Mostly Cloudy
27	1/2/2012 3:00	3.7	-1.5	69	33	25.0	99.30	Mostly Cloudy
...	...	...	...	...	...	...	...	...
8705	12/28/2012 17:00	-8.6	-12.0	76	26	25.0	101.34	Mainly Clear
8753	12/30/2012 17:00	-12.1	-15.8	74	28	25.0	101.26	Mainly Clear
8755	12/30/2012 19:00	-13.4	-16.5	77	26	25.0	101.47	Mainly Clear
8759	12/30/2012 23:00	-12.1	-15.1	78	28	25.0	101.52	Mostly Cloudy
8760	12/31/2012 0:00	-11.1	-14.4	77	26	25.0	101.51	Cloudy
308 rows × 8 columns'''


data.groupby('Weather').mean()

'''Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa
Weather						
Clear	6.825716	0.089367	64.497738	10.557315	30.153243	101.587443
Cloudy	7.970544	2.375810	69.592593	16.127315	26.625752	100.911441
Drizzle	7.353659	5.504878	88.243902	16.097561	17.931707	100.435366
Drizzle,Fog	8.067500	7.033750	93.275000	11.862500	5.257500	100.786625
Drizzle,Ice Pellets,Fog	0.400000	-0.700000	92.000000	20.000000	4.000000	100.790000
Drizzle,Snow	1.050000	0.150000	93.500000	14.000000	10.500000	100.890000
Drizzle,Snow,Fog	0.693333	0.120000	95.866667	15.533333	5.513333	99.281333
Fog	4.303333	3.159333	92.286667	7.946667	6.248000	101.184067
Freezing Drizzle	-5.657143	-8.000000	83.571429	16.571429	9.200000	100.202857
Freezing Drizzle,Fog	-2.533333	-4.183333	88.500000	17.000000	5.266667	100.441667
Freezing Drizzle,Haze	-5.433333	-8.000000	82.000000	10.333333	2.666667	100.316667
Freezing Drizzle,Snow	-5.109091	-7.072727	86.090909	16.272727	5.872727	100.520909
Freezing Fog	-7.575000	-9.250000	87.750000	4.750000	0.650000	102.320000
Freezing Rain	-3.885714	-6.078571	84.642857	19.214286	8.242857	99.647143
Freezing Rain,Fog	-2.225000	-3.750000	89.500000	15.500000	7.550000	99.945000
Freezing Rain,Haze	-4.900000	-7.450000	82.500000	7.500000	2.400000	100.375000
Freezing Rain,Ice Pellets,Fog	-2.600000	-3.700000	92.000000	28.000000	8.000000	100.950000
Freezing Rain,Snow Grains	-5.000000	-7.300000	84.000000	32.000000	4.800000	98.560000
Haze	-0.200000	-2.975000	81.625000	10.437500	7.831250	101.482500
Mainly Clear	12.558927	4.581671	60.667142	14.144824	34.264862	101.248832
Moderate Rain,Fog	1.700000	0.800000	94.000000	17.000000	6.400000	99.980000
Moderate Snow	-5.525000	-7.250000	87.750000	33.750000	0.750000	100.275000
Moderate Snow,Blowing Snow	-5.450000	-6.500000	92.500000	40.000000	0.600000	100.570000
Mostly Cloudy	10.574287	3.131174	62.102465	15.813920	31.253842	101.025288
Rain	9.786275	7.042810	83.624183	19.254902	18.856536	100.233333
Rain Showers	13.722340	9.187766	75.159574	17.132979	22.816489	100.404043
Rain Showers,Fog	12.800000	12.100000	96.000000	13.000000	6.400000	99.830000
Rain Showers,Snow Showers	2.150000	-1.500000	76.500000	22.500000	21.700000	101.100000
Rain,Fog	8.273276	7.219828	93.189655	14.793103	6.873276	100.500862
Rain,Haze	4.633333	2.066667	83.333333	11.666667	6.700000	100.540000
Rain,Ice Pellets	0.600000	-0.600000	92.000000	24.000000	9.700000	100.120000
Rain,Snow	1.055556	-0.566667	89.000000	28.388889	11.672222	99.951111
Rain,Snow Grains	1.900000	-2.100000	75.000000	26.000000	25.000000	100.600000
Rain,Snow,Fog	0.800000	0.300000	96.000000	9.000000	6.400000	100.730000
Rain,Snow,Ice Pellets	1.100000	-0.175000	91.500000	23.250000	6.000000	100.105000
Snow	-4.524103	-7.623333	79.307692	20.038462	11.171795	100.536103
Snow Pellets	0.700000	-6.400000	59.000000	35.000000	2.400000	99.700000
Snow Showers	-3.506667	-7.866667	72.350000	19.233333	20.158333	100.963500
Snow Showers,Fog	-10.675000	-11.900000	90.750000	13.750000	7.025000	101.292500
Snow,Blowing Snow	-5.410526	-7.621053	84.473684	34.842105	4.105263	99.704737
Snow,Fog	-5.075676	-6.364865	90.675676	17.324324	4.537838	100.688649
Snow,Haze	-4.020000	-6.860000	80.600000	5.000000	4.640000	100.782000
Snow,Ice Pellets	-1.883333	-3.666667	87.666667	23.833333	7.416667	100.548333
Thunderstorms	24.150000	19.750000	77.000000	7.500000	24.550000	100.230000
Thunderstorms,Heavy Rain Showers	10.900000	9.000000	88.000000	9.000000	2.400000	100.260000
Thunderstorms,Moderate Rain Showers,Fog	19.600000	18.500000	93.000000	15.000000	3.200000	100.010000
Thunderstorms,Rain	20.433333	18.533333	89.000000	15.666667	19.833333	100.420000
Thunderstorms,Rain Showers	20.037500	17.618750	86.375000	18.312500	15.893750	100.233750
Thunderstorms,Rain Showers,Fog	21.600000	18.700000	84.000000	19.666667	9.700000	100.063333
Thunderstorms,Rain,Fog	20.600000	18.600000	88.000000	19.000000	4.800000	100.080000'''

data.groupby('Weather').max()

'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa
Weather							
Clear	9/9/2012 5:00	32.8	20.4	99	33	48.3	103.63
Cloudy	9/9/2012 23:00	30.5	22.6	99	54	48.3	103.65
Drizzle	9/30/2012 3:00	18.8	17.7	96	30	25.0	101.56
Drizzle,Fog	9/30/2012 2:00	19.9	19.1	100	28	9.7	102.07
Drizzle,Ice Pellets,Fog	12/17/2012 9:00	0.4	-0.7	92	20	4.0	100.79
Drizzle,Snow	12/19/2012 18:00	1.2	0.2	95	19	11.3	101.15
Drizzle,Snow,Fog	12/22/2012 3:00	1.1	0.6	98	32	9.7	100.15
Fog	9/22/2012 0:00	20.8	19.6	100	22	9.7	103.04
Freezing Drizzle	2/1/2012 5:00	-2.3	-3.3	93	26	12.9	101.02
Freezing Drizzle,Fog	12/10/2012 5:00	-0.3	-2.3	94	33	8.0	101.27
Freezing Drizzle,Haze	2/1/2012 13:00	-5.0	-7.7	83	11	4.0	100.36
Freezing Drizzle,Snow	3/2/2012 12:00	-3.3	-4.6	94	24	12.9	101.18
Freezing Fog	3/17/2012 6:00	-0.1	-0.3	99	9	0.8	102.85
Freezing Rain	2/1/2012 7:00	0.3	-1.7	92	28	16.1	101.00
Freezing Rain,Fog	12/17/2012 1:00	0.1	-0.9	93	26	9.7	101.01
Freezing Rain,Haze	2/1/2012 15:00	-4.9	-7.4	83	9	2.8	100.41
Freezing Rain,Ice Pellets,Fog	12/17/2012 3:00	-2.6	-3.7	92	28	8.0	100.95
Freezing Rain,Snow Grains	1/13/2012 9:00	-5.0	-7.3	84	32	4.8	98.56
Haze	3/13/2012 23:00	14.1	11.1	86	17	9.7	102.97
Mainly Clear	9/9/2012 9:00	33.0	21.2	99	63	48.3	103.59
Moderate Rain,Fog	12/10/2012 8:00	1.7	0.8	94	17	6.4	99.98
Moderate Snow	12/27/2012 9:00	-4.9	-6.7	93	39	0.8	100.67
Moderate Snow,Blowing Snow	12/27/2012 12:00	-5.4	-6.4	93	41	0.6	100.64
Mostly Cloudy	9/9/2012 2:00	32.4	24.4	100	83	48.3	103.65
Rain	9/5/2012 2:00	22.8	20.4	99	52	48.3	102.26
Rain Showers	9/8/2012 16:00	26.4	23.0	97	41	48.3	102.31
Rain Showers,Fog	10/20/2012 3:00	12.8	12.1	96	13	6.4	99.83
Rain Showers,Snow Showers	12/5/2012 10:00	2.2	-1.2	78	28	24.1	101.11
Rain,Fog	9/30/2012 23:00	21.7	19.5	100	46	9.7	101.77
Rain,Haze	3/13/2012 9:00	5.5	2.9	86	17	9.7	100.61
Rain,Ice Pellets	12/18/2012 5:00	0.6	-0.6	92	24	9.7	100.12
Rain,Snow	4/23/2012 3:00	1.7	0.5	94	52	25.0	101.07
Rain,Snow Grains	12/21/2012 0:00	1.9	-2.1	75	26	25.0	100.60
Rain,Snow,Fog	12/8/2012 21:00	0.8	0.3	96	9	6.4	100.73
Rain,Snow,Ice Pellets	12/21/2012 5:00	1.3	0.1	94	28	6.4	100.47
Snow	4/27/2012 9:00	3.7	0.3	96	57	25.0	102.73
Snow Pellets	11/24/2012 15:00	0.7	-6.4	59	35	2.4	99.70
Snow Showers	3/4/2012 21:00	2.9	-0.7	94	37	48.3	102.50
Snow Showers,Fog	12/29/2012 13:00	-10.0	-11.1	92	22	9.7	102.52
Snow,Blowing Snow	2/25/2012 9:00	-1.4	-2.9	91	48	9.7	100.62
Snow,Fog	3/14/2012 19:00	1.1	0.8	99	35	9.7	102.07
Snow,Haze	2/1/2012 21:00	-3.6	-6.4	81	15	6.4	100.99
Snow,Ice Pellets	3/3/2012 4:00	0.8	-1.7	92	33	11.3	100.96
Thunderstorms	7/4/2012 16:00	26.7	20.1	87	15	25.0	100.62
Thunderstorms,Heavy Rain Showers	5/29/2012 6:00	10.9	9.0	88	9	2.4	100.26
Thunderstorms,Moderate Rain Showers,Fog	7/17/2012 6:00	19.6	18.5	93	15	3.2	100.01
Thunderstorms,Rain	7/23/2012 18:00	21.3	19.1	93	30	24.1	100.83
Thunderstorms,Rain Showers	9/8/2012 4:00	25.5	23.1	98	32	25.0	101.06
Thunderstorms,Rain Showers,Fog	7/31/2012 20:00	22.9	21.3	91	35	9.7	100.64
Thunderstorms,Rain,Fog	7/17/2012 5:00	20.6	18.6	88	19	4.8	100.08'''


data.groupby('Weather').min()

'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa
Weather							
Clear	1/11/2012 1:00	-23.3	-28.5	20	0	11.3	99.52
Cloudy	1/1/2012 17:00	-21.4	-26.8	18	0	11.3	98.39
Drizzle	1/23/2012 21:00	1.1	-0.2	74	0	6.4	97.84
Drizzle,Fog	1/23/2012 20:00	0.0	-1.6	85	0	1.0	98.65
Drizzle,Ice Pellets,Fog	12/17/2012 9:00	0.4	-0.7	92	20	4.0	100.79
Drizzle,Snow	12/17/2012 15:00	0.9	0.1	92	9	9.7	100.63
Drizzle,Snow,Fog	12/18/2012 21:00	0.3	-0.1	92	7	2.4	97.79
Fog	1/1/2012 0:00	-16.0	-17.2	80	0	0.2	98.31
Freezing Drizzle	1/13/2012 10:00	-9.0	-12.2	78	6	4.8	98.44
Freezing Drizzle,Fog	1/1/2012 2:00	-6.4	-9.0	82	6	3.6	98.74
Freezing Drizzle,Haze	2/1/2012 11:00	-5.8	-8.3	81	9	2.0	100.28
Freezing Drizzle,Snow	1/13/2012 3:00	-8.3	-10.4	79	6	2.4	99.19
Freezing Fog	1/22/2012 6:00	-19.0	-22.9	71	0	0.2	101.97
Freezing Rain	1/13/2012 11:00	-6.5	-9.0	81	7	2.8	98.22
Freezing Rain,Fog	1/17/2012 23:00	-6.1	-8.7	82	7	2.8	98.32
Freezing Rain,Haze	2/1/2012 14:00	-4.9	-7.5	82	6	2.0	100.34
Freezing Rain,Ice Pellets,Fog	12/17/2012 3:00	-2.6	-3.7	92	28	8.0	100.95
Freezing Rain,Snow Grains	1/13/2012 9:00	-5.0	-7.3	84	32	4.8	98.56
Haze	1/22/2012 12:00	-11.5	-16.0	68	0	4.8	100.35
Mainly Clear	1/10/2012 11:00	-22.8	-28.0	20	0	12.9	98.67
Moderate Rain,Fog	12/10/2012 8:00	1.7	0.8	94	17	6.4	99.98
Moderate Snow	1/12/2012 15:00	-6.3	-7.6	83	26	0.6	99.88
Moderate Snow,Blowing Snow	12/27/2012 10:00	-5.5	-6.6	92	39	0.6	100.50
Mostly Cloudy	1/1/2012 16:00	-23.2	-28.5	18	0	11.3	98.36
Rain	1/1/2012 18:00	0.3	-5.7	40	0	4.0	97.52
Rain Showers	1/1/2012 22:00	1.6	-7.2	37	0	6.4	98.51
Rain Showers,Fog	10/20/2012 3:00	12.8	12.1	96	13	6.4	99.83
Rain Showers,Snow Showers	11/4/2012 8:00	2.1	-1.8	75	17	19.3	101.09
Rain,Fog	1/23/2012 18:00	0.0	-1.2	83	0	2.0	98.61
Rain,Haze	3/13/2012 7:00	4.0	1.0	81	7	4.0	100.50
Rain,Ice Pellets	12/18/2012 5:00	0.6	-0.6	92	24	9.7	100.12
Rain,Snow	1/10/2012 5:00	0.6	-1.7	81	13	2.4	98.18
Rain,Snow Grains	12/21/2012 0:00	1.9	-2.1	75	26	25.0	100.60
Rain,Snow,Fog	12/8/2012 21:00	0.8	0.3	96	9	6.4	100.73
Rain,Snow,Ice Pellets	12/21/2012 1:00	0.9	-0.7	88	17	4.8	99.85
Snow	1/10/2012 1:00	-16.7	-24.6	41	0	1.0	97.75
Snow Pellets	11/24/2012 15:00	0.7	-6.4	59	35	2.4	99.70
Snow Showers	1/12/2012 7:00	-13.3	-19.3	52	0	2.4	99.49
Snow Showers,Fog	12/26/2012 9:00	-11.3	-12.7	89	7	4.0	100.63
Snow,Blowing Snow	1/13/2012 21:00	-12.0	-16.2	70	24	0.6	98.11
Snow,Fog	12/16/2012 15:00	-10.1	-12.0	77	4	1.2	99.38
Snow,Haze	2/1/2012 17:00	-4.3	-7.2	80	0	4.0	100.61
Snow,Ice Pellets	12/10/2012 3:00	-4.3	-5.9	76	19	2.8	99.40
Thunderstorms	7/16/2012 1:00	21.6	19.4	67	0	24.1	99.84
Thunderstorms,Heavy Rain Showers	5/29/2012 6:00	10.9	9.0	88	9	2.4	100.26
Thunderstorms,Moderate Rain Showers,Fog	7/17/2012 6:00	19.6	18.5	93	15	3.2	100.01
Thunderstorms,Rain	5/25/2012 20:00	19.4	18.2	83	4	16.1	100.19
Thunderstorms,Rain Showers	5/29/2012 16:00	11.0	7.0	68	7	6.4	99.65
Thunderstorms,Rain Showers,Fog	6/29/2012 3:00	19.5	16.1	80	7	9.7	99.71
Thunderstorms,Rain,Fog	7/17/2012 5:00	20.6	18.6	88	19	4.8	100.08'''


data[data['Weather']=='Fog']

'''Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather
0	1/1/2012 0:00	-1.8	-3.9	86	4	8.0	101.24	Fog
1	1/1/2012 1:00	-1.8	-3.7	87	4	8.0	101.24	Fog
4	1/1/2012 4:00	-1.5	-3.3	88	7	4.8	101.23	Fog
5	1/1/2012 5:00	-1.4	-3.3	87	9	6.4	101.27	Fog
6	1/1/2012 6:00	-1.5	-3.1	89	7	6.4	101.29	Fog
...	...	...	...	...	...	...	...	...
8716	12/29/2012 4:00	-16.0	-17.2	90	6	9.7	101.25	Fog
8717	12/29/2012 5:00	-14.8	-15.9	91	4	6.4	101.25	Fog
8718	12/29/2012 6:00	-13.8	-15.3	88	4	9.7	101.25	Fog
8719	12/29/2012 7:00	-14.8	-16.4	88	7	8.0	101.22	Fog
8722	12/29/2012 10:00	-12.0	-13.3	90	7	6.4	101.15	Fog
150 rows × 8 columns'''

