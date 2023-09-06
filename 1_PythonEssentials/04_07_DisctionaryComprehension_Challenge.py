# add a main method
def main():
    print("Hello World")

    # add a string of characters
    string = "AAABBBBCCCCC"
    print(string)
    visitedChar=[]
    for char in string:
        if char not in visitedChar:
            print(f'New character: {char}')
            visitedChar.append(char)
    print(visitedChar)

    art = '''



                                   %%%%%%%%%%%%%%%%%%%                              
                            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                        %%%%%%%%                         %%%%%%%%                   
                    %%%%%%%                                   %%%%%%                
                  %%%%%%                                         %%%%%%             
               %%%%%%                                               %%%%%           
              %%%%%                                                   %%%%%         
            %%%%%                                                       %%%%%       
           %%%%                 %%%%%              %%%%%                  %%%%      
          %%%%                 %%%%%%%            %%%%%%%                  %%%%     
         %%%%                  %%%%%%%            %%%%%%%                   %%%%    
        %%%%                   %%%%%%%            %%%%%%%                    %%%%   
        %%%%                    %%%%%              %%%%%                     %%%%   
       %%%%                                                                   %%%%  
       %%%%                                                                   %%%%  
       %%%%                                                                   %%%%  
       %%%%                                                      %%%%        %%%%   
        %%%%       %%%%%%                                        %%%%%       %%%%   
        %%%%         %%%%                                       %%%%        %%%%    
         %%%%         %%%%                                     %%%%         %%%%    
          %%%%         %%%%%                                  %%%%         %%%%     
           %%%%%         %%%%%                             %%%%%         %%%%%      
            %%%%%          %%%%%%                        %%%%%          %%%%        
              %%%%%           %%%%%%%               %%%%%%%           %%%%%         
                %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
                  %%%%%%%                                        %%%%%              
                     %%%%%%%                                 %%%%%%%                
                         %%%%%%%%%                     %%%%%%%%%                    
                              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                       %%%%%%%%%%%%                                 



    '''
    print(art)

    for char in art:
        #print(f'Visiting character: {char}')
        if char not in visitedChar:
            print(f'New character: {char}')
            visitedChar.append(char)
    print(visitedChar)



if __name__ == "__main__":
    main()