# include <iostream>
# include <vector>
# include <map>
# include <cmath>
# include <algorithm>

using namespace std;

vector<vector<double>> simulate_calibrated_stock_price(double St, double u, double d, int layers){
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
            stockPrice[i][j] = St * pow(u, i-j) * pow(d, j);
        }
    }
    vector<double> last1 = stockPrice.end()[-1];
    vector<double> last2 = stockPrice.end()[-2];

    // use last1 for price calibration
    // insert last 2 into last 1 and sort
    last1.insert(last1.end(), last2.begin(), last2.end());
    sort(last1.begin(), last1.end(), greater<double>());
    last1[layers] = St;

    // build the vector for calibration
    vector<int> caliIndex;
    for(int i = layers; i > -layers-1; i -= 1){
        caliIndex.push_back(i);
    }
    map<int, double> calibration;
    for(int i = 0; i < layers*2+1; i++){
        calibration[caliIndex[i]] = last1[i];
    }
    for(int i = layers; i > -layers-1; i -= 1){
        cout << calibration[i] << ",";
    }

    // indexDiff : power of u - power of d
    for(int i = 0; i < layers+1; i++){
        for(int j = 0; j < i+1; j++){
            int indexDiff = (i-j) - j;
            stockPrice[i][j] = calibration[indexDiff];
        }
    }

    return stockPrice;
}

class Tree_Node{
    public:
    double St;
    vector<double> SmaxLst;
    vector<double> optionValue;
    
    // constructor
    Tree_Node(double St_ij){
        St = St_ij;
    }
};

// double lookback_CRR_put(double StMax, double St, double T, double r, double q, double sigma, int layers, string type){
//     double dt = T/layers;
//     double u = exp(sigma*sqrt(dt));
//     double d = exp(-sigma*sqrt(dt));
//     double p = (exp((r-q)*dt) - d)/(u - d);

//     vector<vector<double>> stockPrice = simulate_calibrated_stock_price(St, u, d, layers);

//     // build Nodes
//     return;
// }


int main(){
    double St = 50;
    double K = 50;
    double r = 0.1;
    double q = 0.05;
    double sigma = 0.4;
    double T = 0.5;
    int layers = 4;

    double dt = T/layers;
    double u = exp(sigma*sqrt(dt));
    double d = exp(-sigma*sqrt(dt));
    double p = (exp((r-q)*dt) - d)/(u - d);

    vector<vector<double>> stockPrice = simulate_calibrated_stock_price(St, u, d, layers);
    for(int i = 0; i < layers+1; i++){
        for(int j = 0; j < i+1; j++){
            cout << stockPrice[i][j] << "," ;
        }
        cout << endl;
    }

    return 0;
}