# include <iostream>
# include <cmath>
# include <vector>
# include <random>

using namespace std;

vector<double> monte_carlo_European(double S0, double K, double r, double q, double sigma, double T, string call_put, int sims, int rep){
    vector<double> meanLst;
    int times = 0;

    default_random_engine generator;
    normal_distribution<double> distribution(log(S0) + (r - q - 0.5*(pow(sigma, 2)))* T, sigma * sqrt(T));

    while(times < rep){
        vector<double> stockSamples;
        for(int i = 0; i < sims; i++){
            double lnSample = distribution(generator);
            // cout << lnSample << endl;
            double sample = exp(lnSample);
            // cout << sample << endl;
            stockSamples.push_back(sample);
        }

        vector<double> optionValue;
        if(call_put == "call"){
            for(int j = 0; j < stockSamples.size(); j++){
                optionValue.push_back(max(stockSamples[j] - K, 0.0));
            }
            double sum = accumulate(begin(optionValue), end(optionValue), 0.0);
            double mean = sum/sims;
            double discounted = mean * exp(-r*T);
            meanLst.push_back(discounted);
            times += 1;
        }
        else{
            for(int l = 0; l < stockSamples.size(); l++){
                optionValue.push_back(max(K - stockSamples[l], 0.0));
            }
            double sum = accumulate(begin(optionValue), end(optionValue), 0.0);
            double mean = sum/sims;
            double discounted = mean * exp(-r*T);
            meanLst.push_back(discounted);
            times += 1;
        }
    }

    double sum_mean = accumulate(begin(meanLst), end(meanLst), 0.0);
    double meanOfRep = sum_mean/20;
    
    double var = 0.0;
    for(int n = 0; n < 20; n++){
        var += (meanLst[n] - meanOfRep) * (meanLst[n] - meanOfRep);
    }
    var = var/20;
    double sdOfRep = sqrt(var);
    double upper = meanOfRep + sdOfRep;
    double lower = meanOfRep - sdOfRep;
    vector<double> results = {meanOfRep, lower, upper};
    cout << "==================================================" << endl;
    cout << "European " << call_put << endl;
    cout << "--------------------------------------------------" << endl;
    cout << "mean : " << meanOfRep << endl;
    cout << "standard error : " << sdOfRep << endl;
    cout << "0.95 confidence interval : [ " << lower << ", " << upper << " ]" << endl;
    cout << endl;
    return results;
}




int main(){
    double S0 = 115;
    double K = 120;
    double r = 0.01;
    double q = 0.02;
    double sigma = 0.5;
    double T = 1;
    int sims = 10000;
    int rep = 20;

    monte_carlo_European(S0, K, r, q, sigma, T, "call", sims, rep);
    monte_carlo_European(S0, K, r, q, sigma, T, "put", sims, rep);

    return 0;
}