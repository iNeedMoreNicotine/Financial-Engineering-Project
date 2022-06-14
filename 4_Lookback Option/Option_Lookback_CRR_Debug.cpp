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

double lookback_CRR_put(double StMax, double St, double T, double r, double q, double sigma, int layers, string option_type){
    double dt = T/layers;
    double u = exp(sigma*sqrt(dt));
    double d = exp(-sigma*sqrt(dt));
    double p = (exp((r-q)*dt) - d)/(u - d);
    vector<vector<double>> stockPrice = simulate_calibrated_stock_price(St, u, d, layers);

    // build Nodes
    vector<vector<Tree_Node>> TreeNodes;
    for(int i = 0; i < layers+1; i++){
        vector<Tree_Node> temp;
        for(int j = 0; j < i+1; j++){
            temp.push_back(Tree_Node(stockPrice[i][j]));
        }
        TreeNodes.push_back(temp);
    }

    // node(0, 0)
    if(StMax >= St){
        TreeNodes[0][0].SmaxLst.push_back(StMax);
    }
    else{
        TreeNodes[0][0].SmaxLst.push_back(St);
    }

    cout << "starting forward tracking..." << endl; 
    // build SmaxLst in each node by forward tracking method...
    for(int i = 1; i < layers+1; i++){
        for(int j = 0; j < i+1; j++){
            if(j == 0){
                for(int k = 0; k < TreeNodes[i-1][j].SmaxLst.size(); k++){
                    if(TreeNodes[i-1][j].SmaxLst[k] >= TreeNodes[i][j].St){
                        // insert if not in the SmaxLst of TreeNodes[i][j]...
                        if(binary_search(TreeNodes[i][j].SmaxLst.begin(), TreeNodes[i][j].SmaxLst.end(), TreeNodes[i-1][j].SmaxLst[k]) == false){
                            // find the insert location !
                            int insert_index = 0;
                            for(int l = 0; l < TreeNodes[i][j].SmaxLst.size(); l++){
                                if(TreeNodes[i][j].SmaxLst[l] < TreeNodes[i-1][j].SmaxLst[k]){
                                    insert_index = l;
                                    break;
                                }
                            }
                            TreeNodes[i][j].SmaxLst.insert(TreeNodes[i][j].SmaxLst.begin() + insert_index, TreeNodes[i-1][j].SmaxLst[k]);
                        }
                    }
                    else{
                        if(binary_search(TreeNodes[i][j].SmaxLst.begin(), TreeNodes[i][j].SmaxLst.end(), TreeNodes[i][j].St) == false){
                            // find the insert location !
                            int insert_index = 0;
                            for(int l = 0; l < TreeNodes[i][j].SmaxLst.size(); l++){
                                if(TreeNodes[i][j].SmaxLst[l] < TreeNodes[i][j].St){
                                    insert_index = l;
                                    break;
                                }
                            }
                            TreeNodes[i][j].SmaxLst.insert(TreeNodes[i][j].SmaxLst.begin() + insert_index, TreeNodes[i][j].St);
                        }
                    }
                }
            }
            else if(j == i){
                for(int k = 0; k < TreeNodes[i-1][j-1].SmaxLst.size(); k++){
                    if(TreeNodes[i-1][j-1].SmaxLst[k] >= TreeNodes[i][j].St){
                        // if not in the SmaxLst of TreeNodes[i][j]...
                        if(binary_search(TreeNodes[i][j].SmaxLst.begin(), TreeNodes[i][j].SmaxLst.end(), TreeNodes[i-1][j-1].SmaxLst[k]) == false){
                            // find the insert location !
                            int insert_index = 0;
                            for(int l = 0; l < TreeNodes[i][j].SmaxLst.size(); l++){
                                if(TreeNodes[i][j].SmaxLst[l] < TreeNodes[i-1][j-1].SmaxLst[k]){
                                    insert_index = l;
                                    break;
                                }
                            }
                            TreeNodes[i][j].SmaxLst.insert(TreeNodes[i][j].SmaxLst.begin() + insert_index, TreeNodes[i-1][j-1].SmaxLst[k]);
                        }
                    }
                    else{
                        if(binary_search(TreeNodes[i][j].SmaxLst.begin(), TreeNodes[i][j].SmaxLst.end(), TreeNodes[i][j].St) == false){
                            // find the insert location !
                            int insert_index = 0;
                            for(int l = 0; l < TreeNodes[i][j].SmaxLst.size(); l++){
                                if(TreeNodes[i][j].SmaxLst[l] < TreeNodes[i][j].St){
                                    insert_index = l;
                                    break;
                                }
                            }
                            TreeNodes[i][j].SmaxLst.insert(TreeNodes[i][j].SmaxLst.begin() + insert_index, TreeNodes[i][j].St);
                        }
                    }
                }
            }
            else{
                for(int k = 0; k < TreeNodes[i-1][j-1].SmaxLst.size(); k++){
                    if(TreeNodes[i-1][j-1].SmaxLst[k] >= TreeNodes[i][j].St){
                        // if not in the SmaxLst of TreeNodes[i][j]...
                        if(binary_search(TreeNodes[i][j].SmaxLst.begin(), TreeNodes[i][j].SmaxLst.end(), TreeNodes[i-1][j-1].SmaxLst[k]) == false){
                            // find the insert location !
                            int insert_index = 0;
                            for(int l = 0; l < TreeNodes[i][j].SmaxLst.size(); l++){
                                if(TreeNodes[i][j].SmaxLst[l] < TreeNodes[i-1][j-1].SmaxLst[k]){
                                    insert_index = l;
                                    break;
                                }
                            }
                            TreeNodes[i][j].SmaxLst.insert(TreeNodes[i][j].SmaxLst.begin(), insert_index, TreeNodes[i-1][j-1].SmaxLst[k]);
                        }
                    }
                    else{
                        if(binary_search(TreeNodes[i][j].SmaxLst.begin(), TreeNodes[i][j].SmaxLst.end(), TreeNodes[i][j].St) == false){
                            // find the insert location !
                            int insert_index = 0;
                            for(int l = 0; l < TreeNodes[i][j].SmaxLst.size(); l++){
                                if(TreeNodes[i][j].SmaxLst[l] < TreeNodes[i][j].St){
                                    insert_index = l;
                                    break;
                                }
                            }
                            TreeNodes[i][j].SmaxLst.insert(TreeNodes[i][j].SmaxLst.begin(), insert_index, TreeNodes[i][j].St);
                        }
                    }
                }
                for(int k = 0; k < TreeNodes[i-1][j].SmaxLst.size(); k++){
                    if(TreeNodes[i-1][j].SmaxLst[k] >= TreeNodes[i][j].St){
                        // if not in the SmaxLst of TreeNodes[i][j]...
                        if(binary_search(TreeNodes[i][j].SmaxLst.begin(), TreeNodes[i][j].SmaxLst.end(), TreeNodes[i-1][j].SmaxLst[k]) == false){
                            // find the insert location !
                            int insert_index = 0;
                            for(int l = 0; l < TreeNodes[i][j].SmaxLst.size(); l++){
                                if(TreeNodes[i][j].SmaxLst[l] < TreeNodes[i-1][j].SmaxLst[k]){
                                    insert_index = l;
                                    break;
                                }
                            }
                            TreeNodes[i][j].SmaxLst.insert(TreeNodes[i][j].SmaxLst.begin() + insert_index, TreeNodes[i-1][j].SmaxLst[k]);
                        }
                    }
                    else{
                        if(binary_search(TreeNodes[i][j].SmaxLst.begin(), TreeNodes[i][j].SmaxLst.end(), TreeNodes[i][j].St) == false){
                            // find the insert location !
                            int insert_index = 0;
                            for(int l = 0; l < TreeNodes[i][j].SmaxLst.size(); l++){
                                if(TreeNodes[i][j].SmaxLst[l] < TreeNodes[i][j].St){
                                    insert_index = l;
                                    break;
                                }
                            }
                            TreeNodes[i][j].SmaxLst.insert(TreeNodes[i][j].SmaxLst.begin() + insert_index, TreeNodes[i][j].St);
                        }
                    }
                }
            }
            if(i == layers){
                for(int k = 0; k < TreeNodes[i][j].SmaxLst.size(); k++){
                    double payoff = max(TreeNodes[i][j].SmaxLst[k] - TreeNodes[i][j].St, 0.0);
                    TreeNodes[i][j].optionValue.push_back(payoff);
                }
            }
        }   
    }
    cout << "forward tracking done." << endl; 

    cout << "starting backward induction..." << endl;
    // backward induction
    int times = 0;
    int i_temp = layers - 1;
    while(times < layers){
        for(int j = 0; j < i_temp+1; j++){
            int ku = 0;
            int kd = 0;
            for(int k = 0; TreeNodes[i_temp][j].SmaxLst.size(); k++){
                bool u_is_found = false;
                // search for ku in the SmaxLst of the upper node in next layer
                // search for self
                for(int l = ku; l < TreeNodes[i_temp+1][j].SmaxLst.size(); l++){
                    if(TreeNodes[i_temp+1][j].SmaxLst[l] == TreeNodes[i_temp][j].SmaxLst[k]){
                        ku = l;
                        u_is_found = true;
                        break;
                    }
                }
                // searh for self*u
                if(u_is_found == false){
                    for(int l = ku; l < TreeNodes[i_temp+1][j].SmaxLst.size(); l++){
                        if(abs(TreeNodes[i_temp+1][j].SmaxLst[l] - TreeNodes[i_temp][j].SmaxLst[k]*u) < pow(10, -8)){
                            ku = l;
                            break;
                        }
                    }
                }
                // search for kd in the SmaxLst of the lower node in next layer
                for(int l = kd; l < TreeNodes[i_temp+1][j+1].SmaxLst.size(); l++){
                    if(TreeNodes[i_temp+1][j+1].SmaxLst[l] == TreeNodes[i_temp][j].SmaxLst[k]){
                        kd = l;
                        break;
                    }
                }
                double discounted = (TreeNodes[i_temp+1][j].optionValue[ku]*p + TreeNodes[i_temp+1][j+1].optionValue[kd]*(1-p)) * exp(-r*dt);
                if(option_type == "American"){
                    discounted = max(TreeNodes[i_temp][j].SmaxLst[k] - TreeNodes[i_temp][j].St, discounted);
                }
                TreeNodes[i_temp][j].optionValue.push_back(discounted);
            }
        }
        i_temp -= 1;
        times += 1;
    }
    cout << "backward induction done." << endl;

    double putValue = TreeNodes[0][0].optionValue[0];
    // cout << "n = " << layers << endl;
    cout << "(CRR Binomial Tree) Price of " << option_type << " Lookback Put : "  << putValue << endl;
    return putValue;
}




int main(){
    double St = 50;
    double T = 0.25;
    double r = 0.1;
    double q = 0;
    double sigma = 0.4;

    double StMax = 50;
    cout << "============================================================" << endl;
    cout << "Lookback Option" << endl;
    cout << "[ Smax,t = " << StMax << " ]" << endl;
    cout << "------------------------------------------------------------" << endl;

    lookback_CRR_put(StMax, St, T, r, q, sigma, 100, "European");
    lookback_CRR_put(StMax, St, T, r, q, sigma, 100, "American");

    // lookback_CRR_put(StMax, St, T, r, q, sigma, 300, "European");
    // lookback_CRR_put(StMax, St, T, r, q, sigma, 300, "American");

    cout << endl;

    return 0;
}