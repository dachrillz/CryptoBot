# CryptoBot

# Scrum/backlog stories

* Define system requirements

* Define quantative trading stategy version 1.0

* Find data, we need data to train our model

* Find a data stream, or an api or likewise where we can import and update algorithms online (real time)

# Project Plan

## Introduction
The efficient market hypothesis (EMH) states that markets are efficient, meaning that all available information is reflected in the prices of assets. There are three types of EMH's defined with respect to the infromation set (Roberts, 1967),

* Weak EMH, where the information set consists of historical data.

* Semi-strong EMH, where the information set includes all public information

* Strong EMH, where the information set consists of all information known to any participant.

A lot of research has been conducted to investigate if stock markets are efficient. This can be done by assuming that the movement of the market is described by a [random walk](https://en.wikipedia.org/wiki/Random_walk). Although it is notoriously hard to predict the stock market, seemingly, people, hedge funds, algorithms, and so on have done it, and will continue to do so.

Cryptocurrencies have started to emerge during the last couple of years. A lot of exchanges has opened lately, making cryptocurrency trading available. Following the crypto market during the last year it would be an understatement to call it extremely volatile. The markets are very volatile with apparently structured bullish and bearish movements. These "gold rush" behaviours can be triggerd by tweets from credible people in the crypto community and other events.

The hypothesis of the project is that the crypto market is not efficient and we will try to see if we can find some strucutre in the market.

## Goal
The goal of this software/data science project is to build a trading bot that can be connected to an api at a cryptocurrency trading exchange and perform automated trading.

## Quantitative trading strategy
This part described the quantitative trading strategy.

#### Theories about the crypto markets that affect the quant strategy

* Relatively small market cap since it's a world wide trading market. This leads to price manipulation.

* Greater [herd behaviour](https://en.wikipedia.org/wiki/Herd_behavior) than in other markets, reinforcing market movements.

* Barrier to exchange crypto currencies to fiat currencies. This leads to higher trading volume within the crypto markets than would be optimal. Hence, this can lead to stronger correlations between crypto currencies.

* More..

#### What algorithms to use?
How to capture correlation. Is linear enough? Just estimate covariance matrix? Is linear not enough? Estiamte ANN? etc etc

## Media driven trading strategy

#### Theories about the crypto markets that affect the media strategy

* See points from "Theories about the crypto markets that affect the quant strategy"

## Web scraping algorithm
E.g. coinmarketcap has a ['soical' page](https://coinmarketcap.com/currencies/cardano/#social) for each currency. Also there are a lot of other forums, platform etc.

## System requirements



## References
Roberts H (1967). Statistical versus Clinical Prediction of the Stock Market. The Center for Research in Security Prices, Chicago: University of Chicago. Unpublished manuscript.
