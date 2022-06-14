# include <iostream>
# include <cmath>
# include <vector>
# include <random>
# include <chrono>


using namespace std;
// lookback option with floating strike
// call payoff = max(Sτ - Smin,τ, 0)
// put payoff = max(Smax,τ − Sτ , 0)
vector<double> lookback_MC_call(double StMin, double St, double time_left_to_maturity, double r, double q, double sigma, int n, int sims, int rep){
    double dt = time_left_to_maturity/n;
    int times = 0;
    
    default_random_engine generator;
    generator.seed(chrono::system_clock::now().time_since_epoch().count());
    normal_distribution<double> distribution((r - q - 0.5*(pow(sigma, 2)))*dt, sigma*sqrt(dt));

    vector<double> means;
    while(times < rep){
        vector<double> optionValue;

        for(int i = 0; i < sims; i++){
            double minPrice = StMin;
            vector<double> stockPrices;
            stockPrices.push_back(log(St));

            for(int j = 1; j < n+1; j++){
                double dlnS = distribution(generator);
                double sample = stockPrices[j-1] + dlnS;
                stockPrices.push_back(sample);
            }
            for(int k = 0; k < n+1; k++){
                stockPrices[k] = exp(stockPrices[k]);
                if(stockPrices[k] < minPrice){
                    minPrice = stockPrices[k];
                }
            }
            // for each loop, single price path is simulated...
            double callValue = max(stockPrices[n] - minPrice, 0.0)*exp(-r * time_left_to_maturity);
            // cout << putValue << endl;
            optionValue.push_back(callValue);
            }
        
        double sum = 0;
        for(int i = 0; i < sims; i++){
            sum += optionValue[i];
        }
        double mean = sum/sims;
        means.push_back(mean);
        times += 1;
        }
    
    double sum_means = 0;
    for(int l = 0; l < rep; l++){
        sum_means += means[l];
    }
    double meanOfRep = sum_means/rep;
    
    double var = 0.0;
    for(int n = 0; n < rep; n++){
        var += (means[n] - meanOfRep) * (means[n] - meanOfRep);
    }
    var = var/rep;
    double sdOfRep = sqrt(var);
    double upper = meanOfRep + 2*sdOfRep;
    double lower = meanOfRep - 2*sdOfRep;
    vector<double> results = {meanOfRep, lower, upper};
    cout << "==================================================" << endl;
    cout << "Lookback Option : European call " << endl;
    cout << "[ Smin,t = "<< StMin << " ]" << endl;
    cout << "--------------------------------------------------" << endl;
    cout << "mean : " << meanOfRep << endl;
    cout << "standard error : " << sdOfRep << endl;
    cout << "0.95 confidence interval : [ " << lower << ", " << upper << " ]" << endl;
    cout << endl;
    return results;
}

vector<double> lookback_MC_put(double StMax, double St, double time_left_to_maturity, double r, double q, double sigma, int n, int sims, int rep){
    double dt = time_left_to_maturity/n;
    int times = 0;
    
    default_random_engine generator;
    generator.seed(chrono::system_clock::now().time_since_epoch().count());
    normal_distribution<double> distribution((r - q - 0.5*(pow(sigma, 2)))*dt, sigma*sqrt(dt));

    vector<double> means;
    while(times < rep){
        vector<double> optionValue;

        for(int i = 0; i < sims; i++){
            double maxPrice = StMax;
            vector<double> stockPrices;
            stockPrices.push_back(log(St));

            for(int j = 1; j < n+1; j++){
                double dlnS = distribution(generator);
                double sample = stockPrices[j-1] + dlnS;
                stockPrices.push_back(sample);
            }
            for(int k = 0; k < n+1; k++){
                stockPrices[k] = exp(stockPrices[k]);
                if(stockPrices[k] > maxPrice){
                    maxPrice = stockPrices[k];
                }
            }
            // for each loop, single price path is simulated...
            double putValue = max(maxPrice - stockPrices[n], 0.0)*exp(-r * time_left_to_maturity);
            // cout << putValue << endl;
            optionValue.push_back(putValue);
            }
        
        double sum = 0;
        for(int i = 0; i < sims; i++){
            sum += optionValue[i];
        }
        double mean = sum/sims;
        means.push_back(mean);
        times += 1;
        }
    
    double sum_means = 0;
    for(int l = 0; l < rep; l++){
        sum_means += means[l];
    }
    double meanOfRep = sum_means/rep;
    
    double var = 0.0;
    for(int n = 0; n < rep; n++){
        var += (means[n] - meanOfRep) * (means[n] - meanOfRep);
    }
    var = var/rep;
    double sdOfRep = sqrt(var);
    double upper = meanOfRep + 2*sdOfRep;
    double lower = meanOfRep - 2*sdOfRep;
    vector<double> results = {meanOfRep, lower, upper};
    cout << "==================================================" << endl;
    cout << "Lookback Option : European put " << endl;
    cout << "[ Smax,t = "<< StMax << " ]" << endl;
    cout << "--------------------------------------------------" << endl;
    cout << "mean : " << meanOfRep << endl;
    cout << "standard error : " << sdOfRep << endl;
    cout << "0.95 confidence interval : [ " << lower << ", " << upper << " ]" << endl;
    cout << endl;
    return results;
}



int main(){
    double St = 50;
    double T = 0.25;
    double r = 0.1;
    double q = 0;
    double sigma = 0.4;
    int n = 100;
    int sims = 10000;
    int rep = 100;

    lookback_MC_call(30, St, T, r, q, sigma, n, sims, rep);
    lookback_MC_call(40, St, T, r, q, sigma, n, sims, rep);
    lookback_MC_call(50, St, T, r, q, sigma, n, sims, rep);
    
    lookback_MC_put(50, St, T, r, q, sigma, n, sims, rep);
    lookback_MC_put(60, St, T, r, q, sigma, n, sims, rep);
    lookback_MC_put(70, St, T, r, q, sigma, n, sims, rep);
}