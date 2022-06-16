# include <iostream>
# include <cmath>
# include <vector>
# include <random>
# include <chrono> 

using namespace std;

vector<double> monte_carlo_European(double S0, double K, double T, double r, double q, double sigma, string call_put, int sims, int rep){
    vector<double> meanLst;
    int times = 0;

    default_random_engine generator;
    generator.seed(chrono::system_clock::now().time_since_epoch().count());
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
            for(int j = 0; j < sims; j++){
                optionValue.push_back(max(stockSamples[j] - K, 0.0));
            }
            double sum = 0;
            for(int k = 0; k < sims; k++){
                sum += optionValue[k];
            }
            double mean = sum/sims;
            double discounted = mean * exp(-r*T);
            meanLst.push_back(discounted);
            times += 1;
        }
        else{
            for(int l = 0; l < sims; l++){
                optionValue.push_back(max(K - stockSamples[l], 0.0));
            }
            double sum = 0;
            for(int k = 0; k < sims; k++){
                sum += optionValue[k];
            }
            double mean = sum/sims;
            double discounted = mean * exp(-r*T);
            meanLst.push_back(discounted);
            times += 1;
        }
    }
    
    
    double sum_mean = 0;
    for(int i = 0; i < rep; i++){
        sum_mean += meanLst[i];
    }
    double meanOfRep = sum_mean/rep;

    double var = 0.0;
    for(int n = 0; n < rep; n++){
        var += (meanLst[n] - meanOfRep) * (meanLst[n] - meanOfRep);
    }
    var = var/rep;
    double sdOfRep = sqrt(var);
    double upper = meanOfRep + 2*sdOfRep;
    double lower = meanOfRep - 2*sdOfRep;
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
    double K = 115;
    double r = 0.01;
    double q = 0.02;
    double sigma = 0.5;
    double T = 1;
    int sims = 50000;
    int rep = 30;

    monte_carlo_European(S0, K, T, r, q, sigma, "call", sims, rep);
    monte_carlo_European(S0, K, T, r, q, sigma, "put", sims, rep);

    return 0;
}