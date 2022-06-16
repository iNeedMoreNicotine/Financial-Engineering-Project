# include <iostream>
# include <cmath>
# include <vector>

using namespace std;

double binomial_prob(int n, int j, double p){
    // n!/j!
    double temp1[n-j];
    for(int i = 0; i < n-j; i++){
        temp1[i] = log(n-i);
    }
    double sum1 = 0;
    for(int i = 0; i < n-j; i++){
        sum1 += temp1[i];
    }
    
    // (n-j)!
    double temp2[n-j];
    for(int i = 0; i < n-j; i++){
        temp2[i] = log(n-j-i);
    }
    double sum2 = 0;
    for(int i = 0; i < n-j; i++){
        sum2 += temp2[i];
    }
    double sumTerms = sum1 - sum2 + (n-j)*log(p) + j*log(1-p);

    return exp(sumTerms);
}

double binomial_European(double S0, double K, double T, double r, double q, double sigma, int layers, string call_put){
    double dt = T/layers;
    double u = exp(sigma*sqrt(dt));
    double d = exp(-sigma*sqrt(dt));
    double p = (exp((r-q)*dt) - d)/(u - d);

    vector<double> stockPrice;
    for(int j = 0; j < layers+1; j++){
        stockPrice.push_back((S0 * pow(u, layers-j) * pow(d, j)));
    }

    if(call_put == "call"){
        vector<double> callPrice;
        for(int j = 0; j < layers+1; j++){
            callPrice.push_back(max(stockPrice[j] - K, 0.0));
       }
       int times = 0;
       int i_temp = layers-1;
       while(times < layers){
            for(int j = 0; j < i_temp+1; j++){
                callPrice[j] = (callPrice[j]*p + callPrice[j+1]*(1-p)) * exp(-r*dt);
            }
            i_temp -= 1;
            times += 1;
        }

        cout << "(CRR Binomial Tree) Price of European " << call_put << " : " << callPrice[0] << endl;
        return callPrice[0];
    }
    else{
        vector<double> putPrice;
        for(int j = 0; j < layers+1; j++){
            putPrice.push_back(max(K - stockPrice[j], 0.0));
       }
       int times = 0;
       int i_temp = layers-1;
       while(times < layers){
            for(int j = 0; j < i_temp+1; j++){
                putPrice[j] = (putPrice[j]*p + putPrice[j+1]*(1-p)) * exp(-r*dt);
            }
            i_temp -= 1;
            times += 1;
        }
        cout << "(CRR Binomial Tree) Price of European " << call_put << " : " << putPrice[0] << endl;
        return putPrice[0];
    }
}

double binomial_American(double S0, double K, double T, double r, double q, double sigma, int layers, string call_put){
    double dt = T/layers;
    double u = exp(sigma*sqrt(dt));
    double d = exp(-sigma*sqrt(dt));
    double p = (exp((r-q)*dt) - d)/(u - d);

    // simulate stock price
    vector<vector<double>> stockPrice;
    for(int i = 0; i < layers+1; i++){
        vector<double> temp;
        for(int j = 0; j < i+1; j++){
            temp.push_back(0);
        }
        stockPrice.push_back(temp);
    }
    for(int i = 0; i < layers+1; i++){
        for(int j = 0; j < i+1; j++){
            stockPrice[i][j] = S0 * pow(u, i-j) * pow(d, j);
        }
    }

    if(call_put == "call"){
        // calculate terminal payoff
        vector<double> callPrice;
        for(int j = 0; j < layers+1; j++){
            callPrice.push_back(max(stockPrice[layers][j] - K, 0.0));
        }
        int times = 0;
        int i_temp = layers-1;
        while(times < layers){
            vector<double> xValue;
            for(int j = 0; j < i_temp+1; j++){
                callPrice[j] = (callPrice[j]*p + callPrice[j+1]*(1-p)) * exp(-r*dt);
            // calculate excersise value and compare it to holding value...
            }
            for(int k = 0; k < i_temp-1; k++){
                xValue.push_back(max(stockPrice[i_temp][k] - K, 0.0));
                callPrice[k] = max(callPrice[k], xValue[k]);
            }
            i_temp -= 1;
            times += 1;
        }
        cout << "(CRR Binomial Tree) Price of American " << call_put << " : " << callPrice[0] << endl;
        return callPrice[0];
    }
    else{
        vector<double> putPrice;
        for(int j = 0; j < layers+1; j++){
            putPrice.push_back((K - stockPrice[layers][j], 0.0));
        }

        int times = 0;
        int i_temp = layers-1;
        while(times < layers){
            vector<double> xValue;
            for(int j = 0; j < i_temp+1; j++){
                putPrice[j] = (putPrice[j]*p + putPrice[j+1]*(1-p)) * exp(-r*dt);
            // calculate excersise value and compare it to holding value...
            }
            for(int k = 0; k < i_temp+1; k++){
                xValue.push_back(max(K - stockPrice[i_temp][k], 0.0));
                putPrice[k] = max(putPrice[k], xValue[k]);
            }
            i_temp -= 1;
            times += 1;
        }
        cout << "(CRR Binomial Tree) Price of American " << call_put << " : " << putPrice[0] << endl;
        return putPrice[0];
    }

}




int main(){
    double S0 = 50;
    double K = 50;
    double r = 0.1;
    double q = 0.05;
    double sigma = 0.4;
    double T = 0.5;

    int layers = 2000;
    cout << "============================================================" << endl;
    cout << "n = " << layers << endl; 
    cout << "-------------------------CALL-------------------------" << endl;
    binomial_European(S0, K, T, r, q, sigma, layers, "call");
    binomial_American(S0, K, T, r, q, sigma, layers, "call");
    cout << endl;
    cout << "-------------------------PUT-------------------------" << endl;
    binomial_European(S0, K, T, r, q, sigma, layers, "put");
    binomial_American(S0, K, T, r, q, sigma, layers, "put");

    return 0;
}