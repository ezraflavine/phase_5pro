# Phase 5 Project: Unlocking Safaricom’s Future: Predicting the Stock Price of Kenya's telecom giant

<img width="595" alt="Capture2" src="https://github.com/Yaqi-graphics/Phase-5-project---safaricom/assets/137016696/508484e6-72ad-4cc3-bbef-ff996a316d56">

### Group 8 Members.
Jackline Njuguna
Vitelis Siocha
Angel Atungire
Elsie Ochieng
Flavine Atieno
Evans Machua

## The company:
Safaricom, a telecommunications service provider based in Kenya was established in 1997 as a wholly-owned subsidiary of Telkom Kenya. The company offers a diverse range of services including SMS, voice, data, Internet, and M-PESA services. Safaricom provides high-speed data connectivity facilitating access to email, Internet, and corporate networks via fixed and mobile broadband. The company also offers a variety of devices including mobile handsets, broadband modems, routers, tablets, notebooks, and laptops. With a wide dealership network comprising approximately 2,700 outlets, Safaricom ensures extensive distribution of its products and services to consumers and businesses alike.
 In May 2000, Vodafone Group PLC of the United Kingdom acquired a 40% stake in Safaricom along with management responsibilities. Subsequently, in 2008, the Kenyan government offered 25% of its shares to the public through the Nairobi Securities Exchange.

## Safaricom Stocks.
### Public debut:
Safaricom went public on the Nairobi Securities Exchange (NSE) in June 2008, offering 25% of its shares and trades under the ticker symbol “SCOM”. The initial public offering (IPO) was highly successful, raising over KES 50 billion and setting a record for the largest IPO in East and Central Africa at the time.
### Early Growth:
Following the IPO, SCOM experienced a period of significant growth, reflecting the company's strong performance in the Kenyan mobile market. This impressive growth was driven by factors like increasing mobile phone penetration, expansion of M-PESA mobile money services, and diversification into new areas like broadband and enterprise solutions.

## Challenges and Decline:
From 2015 onwards, SCOM encountered several challenges that impacted its stock performance such as increased competition from other mobile operators, regulatory changes, and economic slowdown in Kenya all which contributed to a decline in the stock price. 
Despite the challenges, Safaricom remains a dominant player in the Kenyan market with a strong brand and established infrastructure. The company is investing in new areas like 5G technology and digital services, which could drive future growth. However, the future performance of SCOM will depend on its ability to navigate the competitive landscape, adapt to regulatory changes, and capitalize on new opportunities.

## Project Overview

### 1. Introduction:
Our project revolves around leveraging time-series analysis to predict Safaricom's stock prices. Using advanced analytics on historical market data and key macroeconomic factors, we aim to extract crucial insights and build a robust predictive model for future stock prices.

### 2. Problem Statement
The challenge lies in the inherent unpredictability of Safaricom's stock movements. Our focus is on constructing a robust predictive model through advanced time-series analysis to unravel critical patterns in Safaricom's historical data. This predictive model aims to offer a reliable forecast of future stock prices, aiding stakeholders in navigating the complex and uncertain financial markets.

### 3. Objectives
Main Objectives
Develop a robust time-series forecasting model for Safaricom's stock prices.

## Specific Objectives
To Identify opportune times to buy and sell Safaricom stocks to maximize returns by analyzing historical data, market trends and economic indicators to pinpoint optimal entry and exit points for various project stakeholders.

To conduct sensitivity analysis to assess how inflation rate variations, interest rate, and GDP affect the model's predictions. This can be achieved by simulating different economic scenarios above and understanding how these changes affect stock price forecasts.

## Data Understanding
This analysis/modelling uses several datasets, which can be found in the data folder in this assignment's GitHub repository. Below are our understanding of the datasets.

### I. Historical Prices
This dataset provides daily historical stock prices and volumes for each stock for a given period of time. The historical price trends are used to indicate the future direction of a stock.

### II. Kenya gdp growth rate
This data set expresses the difference between GDP values from one period to the next as a proportion of the GDP from the earlier period in percentage form and showing the dates.

### III. Central bank interest rates
This dataset shows the interest rate at which Kenya's central bank charges other domestic banks to borrow funds. This rates changes based on the economic changes of our country. 

### IV. Dividend Yield
This data set shows the financial ratio that tells us the percentage of Safaricom shares price that it pays out in dividends each year. 

### V. inflation rate
This dataset measures the average change in prices of safaricom stock paid by customers over a period of time. It shows the percentage at which stock prices increase.

## The Merged data set columns
1. Open price is the first price at which stock trades during market hours
2. The high and low prices reflect the highest and lowest prices the stock reaches
3. The Close price is the closing price during the previous market day.
4. Volume is the number of shares traded in a given period.
5. GDP Growth Rate shows the annual average rate of change of the gross domestic product (GDP) at market prices based on constant local currency, for a given national economy, during a specified period of time.
6. Annual average inflation is the percentage change in the annual average consumer price index (CPI) of the corresponding months.
7. Central Bank Rate shows the interest rate at which a central bank lends money to domestic banks, often in the form of very short-term loans.
8. Dividend Yield shows the measures the annual value of dividends received relative to the market value per share.

## Exploratory Data Analysis
Using the merged dataset we checked the relationship between the columns and visualized the correlation.
![correlation](https://github.com/Yaqi-graphics/Phase-5-project---safaricom/assets/137016696/26fcaf40-27e9-4623-b1b2-8be6d06895d8)

Findings
The 'Close' price demonstrates a strong positive correlation with 'Dividend Yield' (0.81) and a negative correlation with 'GDP Growth Rate' (-0.52). 'Annual Average Inflation' and 'Central Bank Rate' exhibit a significant positive correlation (0.83), while 'RSI' and 'MACD' show a moderate positive correlation (0.58). These insights provide valuable information for understanding potential interdependencies and trends within the dataset.

## Modeling and Regression Results.
### 1. Vector Autoregression
This is a multivariate forecasting algorithm that is used when two or more time series influence each other. In this model we will predict only one time-dependent variable which is the close stock prices. We started by spliting the data into training and testing sets, then we trained our VAR Model in order to make predictions. After making predictions on the test set. We extracted the predicted values and visualized the same. This model gave us a rmse of 2.5715913248554116.
![vector autoregression](https://github.com/Yaqi-graphics/Phase-5-project---safaricom/assets/137016696/ab770e07-4d91-4456-b612-e68af0595ef7)

### 2. Recurrent Neural Network (RNN)
In this model we will be training an RNN by presenting sequential data with learning algorithms to the model and updating its parameters iteratively to minimize the prediction error. By feeding historical sequences of safaricom stocks into the RNN, it learns to capture patterns and dependencies in the data. We therefore started by converting the dataset into sequences, then spliting the data into training and testing sets and trained our RNN Model in order to make predictions. After making predictions on the test set. We extracted the predicted values and visualized the same. This model gave us a rmse of 0.04060818256430719.
![rnn](https://github.com/Yaqi-graphics/Phase-5-project---safaricom/assets/137016696/5c97007f-9a14-4a0b-9a4b-90ff9edda5b5)

### 3. Gated Recurrent Unit (GRU)
This model is a specialized recurrent neural network architecture designed to handle long-term dependencies in time series data. It addresses the vanishing gradient problem, allowing them to capture and retain information over extended sequences. In our model, we started by converting the dataset used into sequences, then we split the data into train and test sets. After this we built our GRU Model and trained this model inorder to make our predictions. This model had an rmse of 0.043226513299977044 and below is the graph.
![gru](https://github.com/Yaqi-graphics/Phase-5-project---safaricom/assets/137016696/921c0435-38a3-4a73-b3e2-ffaef9bf3a2f)

### 4. Long Short-Term Memory (LSTM)
This model is designed to capture and remember long-term dependencies in sequential data. This is crucial for time series data, where patterns may depend on events or information from a significant time ago. In this model, we started by converting the data into a sequence, we then Split the data into training and testing sets and build the LSTM model. We then trained the model and made predictions. This model had an rmse of 0.04380510831495241. Below is our visualization.
![lstm](https://github.com/Yaqi-graphics/Phase-5-project---safaricom/assets/137016696/362b045a-c73e-48b3-b913-2ff3a0f75cb7)

### 5. LSTM - Attention (LSTM-Attention)
We apply an attention model to assign different weights to the input features of the financial time series at each time step. We started by converting the data into a sequence then split the data into training and testing sets and Built the LSTM model.
![LSTM-Attention](https://github.com/Yaqi-graphics/Phase-5-project---safaricom/assets/137016696/0929c08f-efc9-4f9a-aede-18c7c8801932)

## Conclusion
Understanding opportune times to buy and sell Safaricom Stocks: The analysis has provided insights on the trajectory of SCOM stocks, which have experienced a downturn in prices since 2022. Several factors have contributed to this, including a change in management at the company and the ongoing economic slowdown in the country, resulting in a decrease in the amount of stocks traded over time.

Exploring other factors affecting SCOM prices:  Research indicates that various factors influence changes in stock prices with macroeconomic factors such as interest rates, inflation rates, and GDP being significant contributors. By incorporating these factors into our modeling, we were able to develop models with lower RMSE compared to those focused solely on historical prices.
Constructing models with single and multiple variables: We successfully built models while evaluating which variables yielded the best performance. The combination of historical prices, macroeconomic factors, and technical indicators resulted in models that effectively captured fluctuating trends and predicted values while achieving the lowest RMSEs.
The LSTM model achieved the lowest RMSE of… compared to Facebook prophet, GRU, VAR and LSTM-attention models, making it the most suitable model for predicting the short-term movement of SCOM stock.

## Limitations
1.	Stock markets are inherently volatile, influenced by various unpredictable factors such as geopolitical events, economic downturns, and regulatory changes. These fluctuations can affect the accuracy of predictive models and impact investment outcomes.
2.	While we tried to include several variables, there are many other factors that affect the prices of SCOM stock and they need to be taken into account as well to create a model that truly captures the complexities of stock markets and enhances predictive capabilities.
3.	While the LSTM model demonstrated superior performance in this study, its effectiveness may vary under different market conditions. Stakeholders should remain vigilant and continuously evaluate model performance to adapt to changing market dynamics.
   
## Recommendations
1.	Investors should consider holding their SCOM stock position and monitor market performance as the current downturn is still considered to be temporary and the company has potential for a rebound, especially with improvements in the economy. Additionally, individuals considering buying SCOM stock may find the current low prices opportune for investment.
2.	Stakeholders should recognize the significance of factors such as interest and inflation rates, alongside technical indicators, in forecasting SCOM stock prices accurately. By integrating these factors into their analyses, they can better anticipate market movements.
3.	Given its superior performance, stakeholders are encouraged to leverage the LSTM model extensively for SCOM stock price predictions, capitalizing on its accuracy and reliability.
4.	To mitigate risks associated with stock market fluctuations, investors should consider diversifying investment portfolios beyond SCOM stock. Exploring opportunities across various sectors and asset classes can help minimize potential losses and optimize returns.
5.	It is imperative to prioritize the continuous monitoring and updating of the models through regular retraining with fresh data and adjusting parameters based on observed performance. Staying proactive in model maintenance ensures accuracy and effectiveness in navigating dynamic market conditions.





