# 1. Jenkins Pipeline ka Basic Structure (Skeleton)

Jaise hum kisi program me { } brackets ka use karte hain, waise hi Jenkins pipeline ka ek fixed standard format hota hai. Kisi bhi pipeline ko likhne se pehle aapko ye basic dhyan me rakhna hota hai:

Groovy
pipeline {
    agent any // 1. Kahan run karna hai

    stages { // 2. Saare bade kaam (Phases) yahan aayenge
        
        stage('Phase Name') { // 3. Ek specific bada kaam
            steps { // 4. Us bade kaam ko karne ke chhote commands
                // Aapke actual Linux commands yahan aate hain
            }
        }

    }

    post { // 5. Pipeline khatam hone ke baad kya karna hai
        success { }
        failure { }
    }
}

# ##############################################################################

# Iske Main Component Kya Hain?

=> pipeline {}: Ye Jenkins ko batata hai ki yahan se pipeline code shuru ho raha hai. Iske andar hi sab kuch aayega.

=> agent any: Iska matlab hai ki Jenkins server ke paas jo bhi free machine (node/worker) available hai, wahan ye script run kar do.

=> stages {}: Ye aapke pure workflow ka main container hai. Iske andar hum batate hain ki hamare pure process me kitne bade phases honge.

=> stage('Name'): Ek single phase (jaise Code download karna, Test karna, Deploy karna).

=> steps {}: Is stage ke andar actual me kya action lena hai (jaise shell command sh '...' chalana).

=> post {}: Jab saare stages chal chuke hote hain, tab pipeline successful hui ya fail, uske basis par agar koi alert bhejna ho ya message print karna ho, toh wo yahan likhte hain.


# ##############################################################################

