def mainOneDimensional(index):
    print()
    print("    Running Single Variable Financial Analysis")
    print("""
    =====================================================
                      Loop index = 1
    =====================================================
     """)
    loopindex = 1
    
    while True:
        
        data = calldata()
        OneDimensionalMethod(data[index])
        loopindex += 1
        
        time.sleep(6)
        print("""
    ===================================================
                      Loop index = %d"""%loopindex + """
    ===================================================
            """)
    print("Done")