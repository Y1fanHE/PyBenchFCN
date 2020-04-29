from PyBenchFCN import SingleObjectiveProblem as SOP

def set_problem(fcn, n_var):
    if fcn.lower() == "f1" or fcn == "ackley": return SOP.ackleyfcn(n_var=n_var)
    if fcn.lower() == "f2" or fcn == "ackleyn2": return SOP.ackleyn2fcn(n_var=n_var)
    if fcn.lower() == "f3" or fcn == "ackleyn3": return SOP.ackleyn3fcn(n_var=n_var)
    if fcn.lower() == "f4" or fcn == "adjiman": return SOP.adjimanfcn(n_var=n_var)
    if fcn.lower() == "f5" or fcn == "alpinen1": return SOP.alpinen1fcn(n_var=n_var)
    if fcn.lower() == "f6" or fcn == "alpinen2": return SOP.alpinen2fcn(n_var=n_var)
    if fcn.lower() == "f7" or fcn == "bartelsconn": return SOP.bartelsconnfcn(n_var=n_var)
    if fcn.lower() == "f8" or fcn == "beale": return SOP.bealefcn(n_var=n_var)
    if fcn.lower() == "f9" or fcn == "bird": return SOP.birdfcn(n_var=n_var)
    if fcn.lower() == "f10" or fcn == "bohachevskyn1": return SOP.bohachevskyn1fcn(n_var=n_var)
    if fcn.lower() == "f11" or fcn == "bohachevskyn2": return SOP.bohachevskyn2fcn(n_var=n_var)
    if fcn.lower() == "f12" or fcn == "booth": return SOP.boothfcn(n_var=n_var)
    if fcn.lower() == "f13" or fcn == "brent": return SOP.brentfcn(n_var=n_var)
    if fcn.lower() == "f14" or fcn == "brown": return SOP.brownfcn(n_var=n_var)
    if fcn.lower() == "f15" or fcn == "bukinn6": return SOP.bukinn6fcn(n_var=n_var)
    if fcn.lower() == "f16" or fcn == "crossintray": return SOP.crossintrayfcn(n_var=n_var)
    if fcn.lower() == "f17" or fcn == "deckkersaarts": return SOP.deckkersaartsfcn(n_var=n_var)
    if fcn.lower() == "f18" or fcn == "dropwave": return SOP.dropwavefcn(n_var=n_var)
    if fcn.lower() == "f19" or fcn == "easom": return SOP.easomfcn(n_var=n_var)
    if fcn.lower() == "f20" or fcn == "eggcrate": return SOP.eggcratefcn(n_var=n_var)
    if fcn.lower() == "f21" or fcn == "eggholder": return SOP.eggholderfcn(n_var=n_var)
    if fcn.lower() == "f22" or fcn == "exponential": return SOP.exponentialfcn(n_var=n_var)
    if fcn.lower() == "f23" or fcn == "goldsteinprice": return SOP.goldsteinpricefcn(n_var=n_var)
    if fcn.lower() == "f24" or fcn == "gramacylee": return SOP.gramacyleefcn(n_var=n_var)
    if fcn.lower() == "f25" or fcn == "griewank": return SOP.griewankfcn(n_var=n_var)
    if fcn.lower() == "f26" or fcn == "happycat": return SOP.happycatfcn(n_var=n_var)
    if fcn.lower() == "f27" or fcn == "himmelblau": return SOP.himmelblaufcn(n_var=n_var)
    if fcn.lower() == "f28" or fcn == "holdertable": return SOP.holdertablefcn(n_var=n_var)
    if fcn.lower() == "f29" or fcn == "keane": return SOP.keanefcn(n_var=n_var)
    if fcn.lower() == "f30" or fcn == "leon": return SOP.leonfcn(n_var=n_var)
    if fcn.lower() == "f31" or fcn == "levin13": return SOP.levin13fcn(n_var=n_var)
    if fcn.lower() == "f32" or fcn == "matyas": return SOP.matyasfcn(n_var=n_var)
    if fcn.lower() == "f33" or fcn == "mccormick": return SOP.mccormickfcn(n_var=n_var)
    if fcn.lower() == "f34" or fcn == "periodic": return SOP.periodicfcn(n_var=n_var)
    if fcn.lower() == "f35" or fcn == "picheny": return SOP.pichenyfcn(n_var=n_var)
    if fcn.lower() == "f36" or fcn == "powellsum": return SOP.powellsumfcn(n_var=n_var)
    if fcn.lower() == "f37" or fcn == "qing": return SOP.qingfcn(n_var=n_var)
    if fcn.lower() == "f38" or fcn == "quartic": return SOP.quarticfcn(n_var=n_var)
    if fcn.lower() == "f39" or fcn == "rastrigin": return SOP.rastriginfcn(n_var=n_var)
    if fcn.lower() == "f40" or fcn == "ridge": return SOP.ridgefcn(n_var=n_var)
    if fcn.lower() == "f41" or fcn == "rosenbrock": return SOP.rosenbrockfcn(n_var=n_var)
    if fcn.lower() == "f42" or fcn == "salomon": return SOP.salomonfcn(n_var=n_var)
    if fcn.lower() == "f43" or fcn == "schaffern1": return SOP.schaffern1fcn(n_var=n_var)
    if fcn.lower() == "f44" or fcn == "schaffern2": return SOP.schaffern2fcn(n_var=n_var)
    if fcn.lower() == "f45" or fcn == "schaffern3": return SOP.schaffern3fcn(n_var=n_var)
    if fcn.lower() == "f46" or fcn == "schaffern4": return SOP.schaffern4fcn(n_var=n_var)
    if fcn.lower() == "f47" or fcn == "schwefel220": return SOP.schwefel220fcn(n_var=n_var)
    if fcn.lower() == "f48" or fcn == "schwefel221": return SOP.schwefel221fcn(n_var=n_var)
    if fcn.lower() == "f49" or fcn == "schwefel222": return SOP.schwefel222fcn(n_var=n_var)
    if fcn.lower() == "f50" or fcn == "schwefel223": return SOP.schwefel223fcn(n_var=n_var)
    if fcn.lower() == "f51" or fcn == "schwefel": return SOP.schwefelfcn(n_var=n_var)
    if fcn.lower() == "f52" or fcn == "sphere": return SOP.spherefcn(n_var=n_var)
    if fcn.lower() == "f53" or fcn == "styblinskitank": return SOP.styblinskitankfcn(n_var=n_var)
    if fcn.lower() == "f54" or fcn == "sumsquares": return SOP.sumsquaresfcn(n_var=n_var)
    if fcn.lower() == "f55" or fcn == "threehumpcamel": return SOP.threehumpcamelfcn(n_var=n_var)
    if fcn.lower() == "f56" or fcn == "wolfe": return SOP.wolfefcn(n_var=n_var)
    if fcn.lower() == "f57" or fcn == "xinsheyangn1": return SOP.xinsheyangn1fcn(n_var=n_var)
    if fcn.lower() == "f58" or fcn == "xinsheyangn2": return SOP.xinsheyangn2fcn(n_var=n_var)
    if fcn.lower() == "f59" or fcn == "xinsheyangn3": return SOP.xinsheyangn3fcn(n_var=n_var)
    if fcn.lower() == "f60" or fcn == "xinsheyangn4": return SOP.xinsheyangn4fcn(n_var=n_var)
    if fcn.lower() == "f61" or fcn == "zakharov": return SOP.zakharovfcn(n_var=n_var)
    return None