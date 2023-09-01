#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;

//Clase donde se crea el punto y se establece su dimensión, con valores aleatorios.
struct Point{
    vector<float> coords;
    int dim;
    Point(int _dim){
        dim = _dim;
        random_device rd;  
        mt19937 gen(rd());
        uniform_real_distribution<> dis(0, 1.0);
        for (int n = 0; n < dim; ++n){
            coords.push_back(dis(gen));
        }
    }
};

int main(){ 
    vector<Point> points;
    vector<int> dim = {2,10,50,100,500,1000,2000,5000}; //Distancias a probar.
    for(int x = 0; x < dim.size(); x++){
        ofstream outputFile(to_string(dim[x])+".txt"); //Generar un txt con las distancias.  
        for(int i = 0; i < 100; i++){
            Point a(dim[x]);
            points.push_back(a);
        }
        for(int i = 0; i < 100; i++){
            for(int j = i+1; j < 100; j++){
                float dist = 0;
                for(int k = 0; k < dim[x]; k++){
                    dist += pow(points[i].coords[k]-points[j].coords[k],2); //Distancia euclidiana.
                }
                dist = sqrt(dist);
                outputFile << dist << endl; 
            }
        }
        outputFile.close();
        points.clear();
    }    
}