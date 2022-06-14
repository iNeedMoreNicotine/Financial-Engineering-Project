# include <iostream>
# include <cmath>
# include <vector>
# include <random>
# include <chrono>

using namespace std;
// arithmetic average option with fixed strike
// call payoff = max(Save,τ - K, 0)
// put payoff = max(K - Save,τ, 0)

vector<double> average_MC_call(double StAve, double St, double K, double time_elapsed, double time_left_to_maturity, double r, double q, double sigma, int n_prev, int n, int sims, int rep){
    double dt = time_left_to_maturity/n;
    int times = 0;

    default_random_engine generator;
    generator.seed(chrono::system_clock::now().time_since_epoch().count());
    normal_distribution<double> distribution((r - q - 0.5*(pow(sigma, 2)))*dt, sigma*sqrt(dt));

    vector<double> means;
    while(times < rep){
        vector<double> optionValue;

        for(int i = 0; i < sims; i++){
            vector<double> stockPrices;
            stockPrices.push_back(log(St));

            for(int j = 1; j < n+1; j++){
                double dlnS = distribution(generator);
                double sample = stockPrices[j-1] + dlnS;
                stockPrices.push_back(sample);
            }
            for(int k = 0; k < n+1; k++){
                stockPrices[k] = exp(stockPrices[k]);
            }
            // for each loop, single price path is simulated...

            double callValue;
            if(time_elapsed == 0){
                double sum_stockPrice = 0;
                for(int l = 0; l < n+1; l++){
                    sum_stockPrice += stockPrices[l];
                }
                double mean_stockPrice = sum_stockPrice/(n+1);
                callValue = max(mean_stockPrice - K, 0.0)*exp(-r * time_left_to_maturity);
                optionValue.push_back(callValue);
            }
            else{
                double sum_stockPrice = 0;
                for(int l = 1; l < n+1; l++){
                    sum_stockPrice += stockPrices[l];
                }
                double payoff = (StAve*(n_prev + 1) + sum_stockPrice)/(n_prev + n + 1) - K;
                callValue = max(payoff, 0.0) * exp(-r * time_left_to_maturity);
                optionValue.push_back(callValue);
            }
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
    cout << "Average Option : European call " << endl;
    cout << "[ Save,t = "<< StAve << " | " << "time_elapsed = " << time_elapsed << " ]" << endl;
    cout << "--------------------------------------------------" << endl;
    cout << "mean : " << meanOfRep << endl;
    cout << "standard error : " << sdOfRep << endl;
    cout << "0.95 confidence interval : [ " << lower << ", " << upper << " ]" << endl;
    cout << endl;
    return results;
}

vector<double> average_MC_put(double StAve, double St, double K, double time_elapsed, double time_left_to_maturity, double r, double q, double sigma, int n_prev, int n, int sims, int rep){
    double dt = time_left_to_maturity/n;
    int times = 0;

    default_random_engine generator;
    generator.seed(chrono::system_clock::now().time_since_epoch().count());
    normal_distribution<double> distribution((r - q - 0.5*(pow(sigma, 2)))*dt, sigma*sqrt(dt));

    vector<double> means;
    while(times < rep){
        vector<double> optionValue;

        for(int i = 0; i < sims; i++){
            vector<double> stockPrices;
            stockPrices.push_back(log(St));

            for(int j = 1; j < n+1; j++){
                double dlnS = distribution(generator);
                double sample = stockPrices[j-1] + dlnS;
                stockPrices.push_back(sample);
            }
            for(int k = 0; k < n+1; k++){
                stockPrices[k] = exp(stockPrices[k]);
            }
            // for each loop, single price path is simulated...

            double putValue;
            if(time_elapsed == 0){
                double sum_stockPrice = 0;
                for(int l = 0; l < n+1; l++){
                    sum_stockPrice += stockPrices[l];
                }
                double mean_stockPrice = sum_stockPrice/(n+1);
                putValue = max(K - mean_stockPrice, 0.0)*exp(-r * time_left_to_maturity);
                optionValue.push_back(putValue);
            }
            else{
                double sum_stockPrice = 0;
                for(int l = 1; l < n+1; l++){
                    sum_stockPrice += stockPrices[l];
                }
                double payoff = K - (StAve*(n_prev + 1) + sum_stockPrice)/(n_prev + n + 1);
                putValue = max(payoff, 0.0) * exp(-r * time_left_to_maturity);
                optionValue.push_back(putValue);
            }
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
    cout << "Average Option : European put " << endl;
    cout << "[ Save,t = "<< StAve << " | " << "time_elapsed = " << time_elapsed << " ]" << endl;
    cout << "--------------------------------------------------" << endl;
    cout << "mean : " << meanOfRep << endl;
    cout << "standard error : " << sdOfRep << endl;
    cout << "0.95 confidence interval : [ " << lower << ", " << upper << " ]" << endl;
    cout << endl;
    return results;
}





int main(){
    double St = 50;
    double StAve = 50;
    double K = 50;
    double r = 0.1;
    double q = 0.05;
    double sigma = 0.8;
    double time_left_to_maturity = 0.25;
    int sims = 10000;
    int rep = 20;
    int n_prev = 100;
    int n = 100;

    average_MC_call(StAve, St, K, 0, time_left_to_maturity, r, q, sigma, n_prev, n, sims, rep);
    average_MC_call(StAve, St, K, 0.25, time_left_to_maturity, r, q, sigma, n_prev, n, sims, rep);

    average_MC_put(StAve, St, K, 0, time_left_to_maturity, r, q, sigma, n_prev, n, sims, rep);
    average_MC_put(StAve, St, K, 0.25, time_left_to_maturity, r, q, sigma, n_prev, n, sims, rep);

    return 0;
}