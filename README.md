# ARIMA Time Series Analysis for Energy Demand Forecasting

by Christina Vavoulis and Julia Napolitano

This time-series forecasting project is written in Python using data from the Energy Information Administration (EIA)

(In Progress...)

### Why predict energy consumption long-term?

As we shift towards electrification to supply our power needs, our need to accurately predict demand heightens. Electricity, by and large, must be used as it is produced- since electricity cannot currently be stored in large amounts for any useful period of time.  If demand surges unexpectedly, there needs to be enough means for production to meet the demand in that instant. 

With accurate forecasting of energy demands, we can accurately plan to scale our production.

This model could be applied to usage data for a specific building, industry (industrial, commercial, residential), utility service territory, or any regional planning for electricity generation. It could be used to predict demand for planning the capacity of a microgrid/distributed generation system, i.e. for the growing number of Community Choice Aggregation (CCA) power providers. 

### Assumptions and definitions

#### Primary energy
Energy in the form that it is first accounted for in a statistical energy balance, before any transformation to secondary or tertiary forms of energy. For example, coal can be converted to synthetic gas, which can be converted to electricity; in this example, coal is primary energy, synthetic gas is secondary energy, and electricity is tertiary energy.

#### Primary fuels
Fuels that can be used continuously. They can sustain the boiler sufficiently for the production of electricity. Natural gas, coal, petroleum, and renewable sources like solar, wind, and hydropower.

##### source: https://www.eia.gov/opendata/qb.php?category=0

By looking at "primary energy consumption", we are not isolating electricity consumption, but rather all fuel consumption, whether it was used for electricity production or directly for heating, transportation, or fueling industrial machinery. This gives us an objective look at how much energy units were consumed, and how much would be needed to provide a completely electric future, as many regions set aggressive goals towards 100% renewable energy. 

### What are the uncertainties and shortcomings of this model?

This model only looks at two variables: DATE and TOTAL ENERGY CONSUMPTION. It projects future trends based on past trends. The output is not predictions of what will happen, but rather modeled projections of what may happen given certain assumptions and methodologies.

Energy market projections are subject to much uncertainty, as many of the events that shape energy markets and future developments in technologies, demographics, and resources cannot be foreseen with certainty. For example, it is unlikely that US economic growth, population growth, cost of resources, availability of resources, legislation (Clean Power Plan), and emerging technology will have a constant rate of change compared to the past 40 years.

That being said, sometimes a simpler model is better than a more complicated model. If we start to postulate on how legislation and emerging technology will change, it adds more layers of uncertainty to our projections. This model claims: legislation, emerging technology, population growth, and economic fluctuations have impacted energy consumption in the past 40 years, yet we can attain a relatively stable model of growth.

If nothing else, the model can be used as baseline test model if legislation, population grown, economic variability, and efficiency improvements continue to change at the same rate as they have previously.

### How does the ARIMA model work?


### How to use it with your own data?

#### Data cleansing: index, column headers, datetime, float
