from flask import Flask , render_template , request 
import sys
import numpy
app = Flask(__name__)

app.secret_key = "hello"


@app.route("/")
def index():
    return render_template("index.html")


#trapping rainwater
@app.route("/algo_0" , methods = ["POST", "GET"])
def algo_():
    if request.method == "POST":
        array = request.form["array"]
        arr = numpy.fromstring(array, dtype=int, count=-1, sep=',')
        n = len(arr)
        res = arr[0]
        size = n - 1
        prev = arr[0]
        prev_index = 0
        water = 0
        temp = 0
        for i in range(1, size + 1):
    
            if (arr[i] >= prev):
                prev = arr[i]
                prev_index = i
                temp = 0
            else:
                water += prev - arr[i]
                temp += prev - arr[i]
    
        if (prev_index < size):
            water -= temp
            prev = arr[size]
            for i in range(size, prev_index - 1, -1):
                if (arr[i] >= prev):
                    prev = arr[i]
                else:
                    water += prev - arr[i]

        return render_template("output.html" , output = water)
    return render_template("algo_0.html")

#Maximum subarray sum.
@app.route("/algo_1" , methods=["POST","GET"])
def algo_1():
    if request.method == "POST":
        array = request.form["array"]
        a = numpy.fromstring(array, dtype=int, count=-1, sep=',')
        size = len(a)
        max_so_far = -sys.maxsize - 1
        max_ending_here = 0
        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
    
            if max_ending_here < 0:
                max_ending_here = 0  
        return render_template("output.html" , output = max_ending_here)

    return render_template("algo_1.html")

#triplets with a given sum.
@app.route("/algo_2" , methods = ["POST" , "GET"])
def algo_2():

    if(request.method == "POST"):     

        target_sum = request.form["target"]
        target_sum = int(target_sum)
        array = request.form["array"]
        A = numpy.fromstring(array, dtype=int, count=-1, sep=',')   
        arr_size = len(A)
        if(arr_size<3):
            return render_template("output.html" , output = "Please enter a valid input")
        A.sort()
        for i in range(0, arr_size-2):
        
            l = i + 1
            r = arr_size-1
            while (l < r):
                if( A[i] + A[l] + A[r] == target_sum):
                    anwser = (A[i],A[l],A[r])
                    anwser = " ".join(str(x) for x in anwser)
                    return render_template("output.html" , output = anwser)
                elif (A[i] + A[l] + A[r] < target_sum):
                    l += 1
                else: 
                    r -= 1
        return render_template("output.html" , output = "There is no 3 elements with the given sum")
     
    return render_template("algo_2.html")

#Maximum profit from selling and buying stocks
@app.route("/algo_3" , methods = ["POST", "GET"])
def algo_3():
    if request.method == "POST":
        array = request.form["array"]
        prices = numpy.fromstring(array, dtype=int, count=-1, sep=',')
        n = len(prices)
        cost = 0
        maxcost = 0 
        if (n == 0):
            return 0
        min_price = prices[0]
        for i in range(n):
            min_price = min(min_price, prices[i])
            cost = prices[i] - min_price
            maxcost = max(maxcost, cost)
            return render_template("output.html" , output = maxcost)
    return render_template("algo_3.html")

#Majority element in a arary
@app.route("/algo_4" , methods ={"POST","GET"})
def algo_4():
    if request.method == "POST":
        array = request.form["array"]
        arr = numpy.fromstring(array, dtype=int, count=-1, sep=',')
        size = len(arr)
        m = {}
        for i in range(size):
            if arr[i] in m:
                m[arr[i]] += 1
            else:
                m[arr[i]] = 1
        count = 0
        for key in m:
            if m[key] > size / 2:
                count = 1
                return render_template("output.html" , output = key)
                break
        if(count == 0):
            return render_template("output.html" , output = "No Majority element in the array,Enter again")

    return render_template("algo_4.html")


@app.route("/output", methods ={"POST","GET"})
def output():
    return render_template("output.html")



if __name__ == "__main__":
    app.run(debug = True)