#-*- encoding: utf-8 -*-

import os

path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(path + os.sep + '..')

from helper import str_helper, file_helper, mail_helper, date_helper, log_helper




def build_maven_code(glocd, versions):
    for i in abc.split('\n'):
        ls = i.strip().replace('"','').split(' ')
        if len(ls) <= 1:
            continue
        lss = ls[1].split(':')
        sss = '''   <dependency>
        <groupId>%s</groupId>
        <artifactId>%s</artifactId>
        <version>%s</version>
    </dependency>'''  % (lss[0], lss[1], lss[2].replace('$', ''))
        print sss



if __name__ == '__main__':
    
    glocd = ''' 
    compile "org.springframework:spring-webmvc:$springVersion"
compile "org.springframework:spring-jdbc:$springVersion"
compile "com.h2database:h2:$h2Version"
compile "org.hibernate:hibernate-validator:$hibernateValidatorVersion"
compile "org.apache.commons:commons-lang3:$commonsLangVersion"

compile "javax.servlet:jstl:$jstlVersion"
providedCompile "javax.servlet:javax.servlet-api:$servletApiVersion"
providedCompile "javax.servlet.jsp:jsp-api:$jspApiVersion"
providedCompile "javax.el:javax.el-api:$jspElVersion"

testCompile "junit:junit-dep:$junitVersion"
testCompile "org.springframework:spring-test:$springVersion"
testCompile "org.mockito:mockito-core:$mockitoVersion"
testCompile "org.hamcrest:hamcrest-library:$hamcrestVersion"
    '''
    build_maven_code(glocd, '')