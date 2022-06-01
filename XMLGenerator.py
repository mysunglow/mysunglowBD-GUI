from accountDict import *
from detailsDict import *
from fabricDict import *
import datetime
from logger import *

genLogger = Logger()


class XMLGenerator:
    date = datetime.date.today().strftime("%m/%d/%y")
    time = datetime.datetime.now().strftime("%I:%M:%S")

    def testOrder(self, orderArray):
        for order in orderArray:
            print(order)
            print('\n')

    def handleChain(self, blindData):
        returnList = []
        chainDrop = blindData.get('chainDrop')
        length = float(blindData.get('length'))
        controlColorPower = blindData.get('controlColorPower')
        shade = blindData.get('shade')

        chainLength = -1

        if(chainDrop == 'Custom'):
            chainDropLength = float(blindData.get('chainDropLength'))
            chainLength = chainDropLength
        elif(length <= 30):
            chainLength = round(length, 0)
        elif(length <= 40):
            chainLength = round(length-5, 0)
        else:
            chainLength = round(length-10, 0)

        # STAINLESS STEEL in all shades
        if (controlColorPower == "Stainless Steel"):
            if(chainLength >= 45 and chainLength <= 46):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='45-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL45'/>")
            elif(chainLength >= 49 and chainLength <= 51):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='50-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL50'/>")
            elif(chainLength >= 54 and chainLength <= 56):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='55-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL55'/>")
            elif(chainLength >= 59 and chainLength <= 61):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='60-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL60'/>")
            elif(chainLength >= 64 and chainLength <= 66):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='65-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL65'/>")
            elif(chainLength >= 69 and chainLength <= 71):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='70-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL70'/>")
            elif(chainLength >= 74 and chainLength <= 76):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='75-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL75'/>")
            elif(chainLength >= 79 and chainLength <= 81):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='80-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL80'/>")
            elif(chainLength >= 84 and chainLength <= 86):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='85-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL85'/>")
            else:
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='SS-Stainless steel'  ChoiceCode_='Y_COP2_SS'/>")

        elif(controlColorPower != "Stainless Steel"):
            #   if Plastic Chain (IN NOT INT AND ROMAN)
            if(shade != "INTERLUDE SHADE" and shade != "ROMAN SHADE"):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='BC-Bead Chain'  ChoiceCode_='Y_CT2_BEAD'/>")
                # BEAD CHAIN NO SIZES HENCE COP 2 NO
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='.-N/A'  ChoiceCode_='Y_COP2_NO'/>")

        #   If Plastic Chain (In int and SOMETHING TODO)
            elif((shade == "INTERLUDE SHADE") or (shade == "ROMAN SHADE")):
                if(chainLength < 39):
                    returnList.append(
                        f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"24'-Plastic Loop\"  ChoiceCode_=\"Y_COP2_PL2\"/>")
                elif(chainLength < 51):
                    returnList.append(
                        f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"36'-Plastic Loop\"  ChoiceCode_=\"Y_COP2_PL3\"/>")
                elif(chainLength < 63):
                    returnList.append(
                        f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"48'-Plastic Loop\"  ChoiceCode_=\"Y_COP2_PL4\"/>")
                elif(chainLength < 75):
                    returnList.append(
                        f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"60'-Plastic Loop\"  ChoiceCode_=\"Y_COP2_PL5\"/>")
                else:
                    returnList.append(
                        f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"72'-Plastic Loop\"  ChoiceCode_=\"Y_COP2_PL6\"/>")

        return returnList

    def handleCord(self, blindData):
        returnList = []
        chainDrop = blindData.get('chainDrop')
        length = float(blindData.get('length'))
        shade = blindData.get('shade')

        chainLength = -1

        if(chainDrop == 'Custom'):
            chainDropLength = float(blindData.get('chainDropLength'))
            chainLength = chainDropLength
        elif(length <= 30):
            chainLength = round(length, 0)
        elif(length <= 40):
            chainLength = round(length-5, 0)
        else:
            chainLength = round(length-10, 0)

        if((shade == "INTERLUDE SHADE" or shade == "ILLUSION SHADE")):
            if(chainLength < 39):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"2'-Cord Loop\"  ChoiceCode_=\"Y_COP2_CL2\"/>")
            elif(chainLength < 51):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"3'-Cord Loop\"  ChoiceCode_=\"Y_COP2_CL3\"/>")
            elif(chainLength < 63):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"4'-Cord Loop\"  ChoiceCode_=\"Y_COP2_CL4\"/>")
            elif(chainLength < 75):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"5'-Cord Loop\"  ChoiceCode_=\"Y_COP2_CL5\"/>")
            elif(chainLength < 87):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"6'-Cord Loop\"  ChoiceCode_=\"Y_COP2_CL6\"/>")
            elif(chainLength < 99):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"7'-Cord Loop\"  ChoiceCode_=\"Y_COP2_CL7\"/>")
            else:
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_=\"8'-Cord Loop\"  ChoiceCode_=\"Y_COP2_CL8\"/>")

        return returnList

    def handleVision(self, blindData):
        returnList = []
        chainDrop = blindData.get('chainDrop')
        length = float(blindData.get('length'))
        controlColorPower = blindData.get('controlColorPower')

        chainLength = -1

        if(chainDrop == 'Custom'):
            chainDropLength = float(blindData.get('chainDropLength'))
            chainLength = chainDropLength
        elif(length <= 30):
            chainLength = round(length, 0)
        elif(length <= 40):
            chainLength = round(length-5, 0)
        else:
            chainLength = round(length-10, 0)

        if(controlColorPower == "Stainless Steel"):
            if(chainLength >= 45 and chainLength <= 46):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='45-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL45'/>")
            elif(chainLength >= 49 and chainLength <= 51):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='50-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL50'/>")
            elif(chainLength >= 54 and chainLength <= 56):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='55-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL55'/>")
            elif(chainLength >= 59 and chainLength <= 61):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='60-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL60'/>")
            elif(chainLength >= 64 and chainLength <= 66):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='65-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL65'/>")
            elif(chainLength >= 69 and chainLength <= 71):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='70-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL70'/>")
            elif(chainLength >= 74 and chainLength <= 76):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='75-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL75'/>")
            elif(chainLength >= 79 and chainLength <= 81):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='80-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL80'/>")
            elif(chainLength >= 84 and chainLength <= 86):
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='85-Loop Stainless Steel'  ChoiceCode_='Y_COP2_SSL85'/>")
            else:
                returnList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Control Option' Choice_='SS-Stainless steel'  ChoiceCode_='Y_COP2_SS'/>")
        else:
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Chain Color" Choice_="{dictVisionColorDesc.get(controlColorPower)}" ChoiceCode_="{dictVisionColorCode.get(controlColorPower)}"/>')

        return returnList

    def blindDetails(self, blindData):
        requiredDetails = ['\n\n<TEDIOrderDetails_Details']

        shade = blindData.get('shade')
        measure = blindData.get('measure')
        width = blindData.get('width')
        length = blindData.get('length')
        fabric = blindData.get('fabric')
        location = blindData.get('shadeID', 'Missing Location')
        # special = blindData.get('specialInstruction')
        controlSystem = blindData.get('controlSystem')
        panel = blindData.get('panel')
        valanceReturn = blindData.get('valanceReturn')

        # Systems Handler
        if(controlSystem == 'Motor'):
            if(shade == 'ROMAN SHADE'):
                shade = 'ROMAN SHADE MOTOR'
            elif(shade == 'SB ROLLER SHADE'):
                shade = 'SB ROLLER SHADE MOTOR'
            elif(shade == 'SB INTERLUDE SHADE'):
                shade = 'SB INTERLUDE SHADE MOTOR'
            elif(shade == 'SB ILLUSION SHADE'):
                shade = 'SB ILLUSION SHADE MOTOR'
            elif(shade == 'SB ILLUSION SHADE'):
                shade = 'VISION SHADE MOTOR'
            elif(shade == 'VISION SHADE'):
                shade = 'VISION SHADE MOTOR'

        elif(controlSystem == 'ZeroGravity'):
            if(shade == 'SB INTERLUDE SHADE'):
                shade = 'SB INTERLUDE SHADE ZEROGRAVITY'
            elif(shade == 'SB ROLLER SHADE'):
                shade = 'SB ZEROGRAVITY'

        elif(controlSystem == 'Neo' or controlSystem == 'Chainless'):
            if(shade == 'SB INTERLUDE SHADE'):
                shade = 'SB INTERLUDE SHADE CHAINLESS'
            elif(shade == 'SB ROLLER SHADE'):
                shade = 'SB CHAINLESS'

        # Special Instructions Handler
        # if(special != None):
        #     special = 'Notes: ' +special + ' | '
        #     if(valanceReturn != 0 and valanceReturn != None):
        #         special = f'{special} | Return: {valanceReturn} | '
        #     special = special.replace('"', ' *Inch* ')
        #     special = special.replace("'", ' *Ft* ')

        quantity = blindData.get('quantity')
        PO = blindData.get('PO')
        valance = blindData.get('valance')
        valanceReturn = blindData.get('valanceReturn')
        chainDrop = blindData.get('chainDrop')
        chainDropLength = blindData.get('chainDropLength')

        # fixedDetails = blindData.get('controlColorPower')

        sideBySide = blindData.get('sideBySide')
        if (sideBySide == None):
            sideBySide = ''
        else:
            sideBySide = '| sideBySide: ' + str(sideBySide)

        if (chainDrop == 'Custom'):
            chainDrop = '| Chaindrop: ' + str(chainDropLength)
        else:
            chainDrop = ''

        # control = blindData.get('controlSystem')
        # turns = blindData.get('turns')

        valance = blindData.get('valance')

        requiredDetails.append(
            f'\nBlindTypeDescription_="{dictBlindDesc.get(shade)}"')
        requiredDetails.append(f'\nBlindTypeCode_="{dictBlind.get(shade)}"')
        requiredDetails.append(f'\nMeasureName_="{dictMeasure.get(measure)}"')

        requiredDetails.append(f'\nMetricMeasurement_="1"')
        requiredDetails.append(f'\nWidth_="{float(width)*25.4}"')
        requiredDetails.append(f'\nDrop_="{float(length)*25.4}"')
        requiredDetails.append(f'\nWidthDisplay_="{width}"')
        requiredDetails.append(f'\nDropDisplay_="{length}"')

        requiredDetails.append(f'\nFabricCode_="{fabricsDict.get(fabric)}"')

        requiredDetails.append(f'\nLocation_="{location}"')

        # if(shade == 'FIXED SHADE'):
        #     requiredDetails.append(f'\nSpecialInstructions_="{special} | Fixed Details: {fixedDetails}"')
        # elif(shade == 'INTERLUDE SHADE' or shade == 'ILLUSION SHADE'):
        #     requiredDetails.append(f'\nSpecialInstructions_="{special} {sideBySide} {chainDrop}"')
        # elif(valance == 'Fabric Valance'):
        #     valanceDrop = blindData.get('valanceFinish').replace('"', ' *Inch* ')
        #     requiredDetails.append(f'\nSpecialInstructions_="{special} Valance Drop: {valanceDrop}  {chainDrop}"')
        # elif (control == "Chain - Vision"):
        #     requiredDetails.append(f'\nSpecialInstructions_="{special} Vision Spring Turns: {turns} {chainDrop}"')
        # else:
        #     requiredDetails.append(f'\nSpecialInstructions_="{special} {chainDrop}"')

        requiredDetails.append(
            f'\nSpecialInstructions_="{self.addSpecIns(blindData)}"')

        requiredDetails.append(f'\nQuantity_="{quantity}"')
        requiredDetails.append(f'\nFabricDescription_="{fabric}"')
        requiredDetails.append(f'\nOrderID_="{PO}"')

        # TODO Delivery Address
        requiredDetails.extend(self.addDelivery())
        # TODO Panel Track Details
        if(shade == "PANEL TRACK"):
            if(panel != None):
                requiredDetails.append(f'\nNumberOfPanels_="{panel}"')
            else:
                requiredDetails.append(f'\nNumberOfPanels_="0"')

            requiredDetails.append(f'\nPanelSize_="{width}"')
            requiredDetails.append(f'\nPanelDrop_="{length}"')

        # Return_ field giving an error on BD? Removing it, I have it in spec ins
        # if(valance == 'Fabric Valance' or valance == 'PVC Valance'):
        #     requiredDetails.append(f'\nReturn_="{valanceReturn}"')

        # Chain Drop
        if(chainDropLength is not None and chainDropLength > 0):
            requiredDetails.append(f'\nChainLength_="{chainDropLength}"')

        # print('Blind Details')
        requiredDetails.append(f'\nIsDetailTwoDayDespatch_="FALSE">')
        return requiredDetails

    def addSpecIns(self, blindData):
        shade = blindData.get('shade')
        special = blindData.get('specialInstruction')
        valance = blindData.get('valance')
        valanceReturn = blindData.get('valanceReturn')
        chainDropLength = blindData.get('chainDropLength')
        fixedDetails = blindData.get('controlColorPower')
        sideBySide = blindData.get('sideBySide')
        control = blindData.get('controlSystem')
        turns = blindData.get('turns')
        zeroGSpring = blindData.get('controlClutchMotor')
        zeroGTurns = blindData.get('controlController')
        lam = blindData.get('liftAssist')

        result = ''

        if(special != None and special != "None" and special != '' and special != ' '):
            special = special.replace('"', ' *Inch* ')
            special = special.replace("'", ' *Ft* ')
            result += special

        if(valance == 'Fabric Valance'):
            result = self.handlePipe(result)
            result += f'{blindData.get("valanceFinish")}'
        elif(valance == 'Fabric Valance w/ Return'):
            result = self.handlePipe(result)
            result += f'{blindData.get("valanceFinish")}, Return: {valanceReturn} Inches'
        elif(valance == 'PVC Valance'):
            result = self.handlePipe(result)
            result += f'Return: {valanceReturn} Inches'

        if(shade == 'SB INTERLUDE SHADE' or shade == 'SB ILLUSION SHADE' or shade == 'INTERLUDE SHADE'):
            if(sideBySide != None and sideBySide != 'None' and sideBySide != ''):
                result = self.handlePipe(result)
                result += f'SideBySide: {sideBySide}'
        elif(shade == 'FIXED SHADE'):
            result = self.handlePipe(result)
            result += f'Fixed Details: {fixedDetails}'

        if (control == "Chain - Vision"):
            result = self.handlePipe(result)
            result += f'Vision Turns: {turns}'

        if(control == 'ZeroGravity' and (zeroGSpring == 'Light' or zeroGSpring == 'Medium' or zeroGSpring == 'Heavy')):
            result = self.handlePipe(result)
            result += f'ZeroG Turns: {round(float(zeroGTurns),2)}'

        if(chainDropLength is not None and chainDropLength > 0):
            result = self.handlePipe(result)
            result += 'Chaindrop: ' + str(chainDropLength)

        if (lam == "true"):
            result = self.handlePipe(result)
            result += f'Turns: {round(float(turns),2)}'

        if(result != None and result != "None" and result != '' and result != ' '):
            result = result.replace('"', ' *Inch* ')
            result = result.replace("'", ' *Ft* ')

        return result

    def handlePipe(self, myString):
        if (len(myString) == 0):
            return myString
        else:
            return f'{myString} | '

    def addDelivery(self):
        # print(self.currentOrder)
        returnList = []

        if (self.currentOrder.get("streetAddress") != None):
            # stringList.append(f'FOUND ADDRESS'
            # pass
            returnList.append(f'\nIsDirectDeliveryBySupplier_="True"')
            returnList.append(
                f'\nDelLine1_="{self.currentOrder.get("streetAddress")}"')
            returnList.append(f'\nDelLine2_="{self.currentOrder.get("unit")}"')
            returnList.append(f'\nDelCity_="{self.currentOrder.get("city")}"')
            # stringList.append(f'\nDelState_="Zor"')
            returnList.append(
                f'\nDelPostCodePart1_="{self.currentOrder.get("postalcode")[0:3]}"')
            returnList.append(
                f'\nDelPostCodePart2_="{self.currentOrder.get("postalcode")[3:7]}"')
            returnList.append(
                f'\nDelFirstName_="{self.currentOrder.get("firstName")}"')
            returnList.append(
                f'\nDelLastName_="{self.currentOrder.get("lastName")}"')
            returnList.append(
                f'\nDelPhone_="{self.currentOrder.get("phone")}"')
            # stringList.append(f'\nDelFax_=""')
            returnList.append(
                f'\nDelCountry_="{self.currentOrder.get("country")}"')

        return returnList

    def addHem(self, blindData):
        resultList = []

        hem = blindData.get('hem')
        hemColor = blindData.get('hemColor')
        hemCaps = blindData.get('hemCaps')
        hemStitched = blindData.get('hemStitched')

        resultList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Hem Type" Choice_="{dictHemDesc.get(hem)}"  ChoiceCode_="{dictHemCode.get(hem)}"/>')
        if(hem != 'Plain Hem'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem cap Color" Choice_="{dictHemCapsDesc.get(hemCaps)}" ChoiceCode_="{dictHemCapsCode.get(hemCaps)}"/>')

        if(hem == 'Slim Bar'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Finish" Choice_="{dictSBColorDesc.get(hemColor)}" ChoiceCode_="{dictSBColorCode.get(hemColor)}"/>')
        elif(hem == 'Accubar' or hem == 'Front Wrapped Accubar'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Finish" Choice_="{dictABColorDesc.get(hemColor)}" ChoiceCode_="{dictABColorCode.get(hemColor)}"/>')
        elif(hem == 'Accurail'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Finish" Choice_="{dictACColorDesc.get(hemColor)}" ChoiceCode_="{dictACColorCode.get(hemColor)}"/>')
        elif(hem == 'Interlude'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Finish" Choice_="{dictInColorDesc.get(hemColor)}" ChoiceCode_="{dictInColorCode.get(hemColor)}"/>')
        elif(hem == 'Illusion'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Finish" Choice_="{dictIllColorDesc.get(hemColor)}" ChoiceCode_="{dictIllColorCode.get(hemColor)}"/>')
        elif(hem == 'SB Deluxe Flat'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Finish" Choice_="{dictDFColorDesc.get(hemColor)}" ChoiceCode_="{dictDFColorCode.get(hemColor)}"/>')
        # TO DO ZERO G Bottom Bar
        elif(hem == 'Zero Gravity Bar'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Finish" Choice_="{dictECColorDesc.get(hemColor)}" ChoiceCode_="{dictECColorCode.get(hemColor)}"/>')

        if(hemStitched == True or hemStitched == 'true'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Option" Choice_="S-Stitched Sides" ChoiceCode_="Y_HO_PHS"/>')

        if(hem == 'Front Wrapped Accubar'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Hem Option" Choice_="WA-Wrapped" ChoiceCode_="Y_HO_WA"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Wrapped" Choice_="WA-Wrapped" ChoiceCode_="Y_BBW_Y"/>')

        return resultList

    def addControl(self, blindData):
        controlPosition = blindData.get('controlPosition')
        controlSystem = blindData.get('controlSystem')
        controlColorPower = blindData.get('controlColorPower')
        controlController = blindData.get('controlController')
        controlClutchMotor = blindData.get('controlClutchMotor')
        controlclutchCover = blindData.get('controlclutchCover')

        tube = blindData.get('tube')
        neo = blindData.get('neo')
        spring = blindData.get('spring')

        shade = blindData.get('shade')

        resultList = [
            f'\n<TEDIOptionList_Details OptionName_="-Control" Choice_="{dictCSystemDesc.get(controlSystem)}" ChoiceCode_="{dictCSystemCode.get(controlSystem)}"/>']

        # Chain
        if(controlSystem == 'Chain'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')

            if (controlColorPower == "Stainless Steel"):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="CH-Metal Chain" ChoiceCode_="Y_COP1_CH10"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="CH-Plastic Chain" ChoiceCode_="Y_COP1_PBC"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Chain Color" Choice_="{dictCColorPowerDesc.get(controlColorPower)}" ChoiceCode_="{dictCColorPowerCode.get(controlColorPower)}"/>')
            if(shade != 'ROMAN SHADE'):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="{dictCControllerDesc.get(controlController)}" ChoiceCode_="{dictCControllerCode.get(controlController)}"/>')

            if(controlClutchMotor == 'R8' and tube == '1 1/2'):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="R5" ChoiceCode_="Y_CLS_5"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="{dictClutchMotorDesc.get(controlClutchMotor)}" ChoiceCode_="{dictClutchMotorCode.get(controlClutchMotor)}"/>')

            if(controlclutchCover != None and controlclutchCover != 'None'):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictClutchCoverDesc.get(controlclutchCover)}" ChoiceCode_="{dictClutchCoverCode.get(controlclutchCover)}"/>')

            resultList.extend(self.handleChain(blindData))

            return resultList

        # Cord
        if(controlSystem == 'Cord' and shade != 'PANEL TRACK'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="CD-Cord Loop" ChoiceCode_="Y_COP1_CL"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="{dictCControllerDesc.get(controlController)}" ChoiceCode_="{dictCControllerCode.get(controlController)}"/>')

            if(controlClutchMotor == 'R8' and tube == '1 1/2'):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="R5" ChoiceCode_="Y_CLS_5"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="{dictClutchMotorDesc.get(controlClutchMotor)}" ChoiceCode_="{dictClutchMotorCode.get(controlClutchMotor)}"/>')

            resultList.extend(self.handleCord(blindData))

            return resultList

        elif(controlSystem == 'Cord' and shade == 'PANEL TRACK'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="CD-Cord Loop" ChoiceCode_="Y_COP1_CL"/>')

            resultList.extend(self.handleCord(blindData))

            return resultList

        elif(controlSystem == 'Wand' and shade == 'PANEL TRACK'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')

            return resultList

        # Motor
        elif(controlSystem == 'Motor'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')
            if(controlClutchMotor == "SG Rechargeable Motor" or controlClutchMotor == "SG Bi-Directional - [SGRM]"):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="5V-Battery" ChoiceCode_="Y_CLT_M5"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="{dictCColorPowerDesc.get(controlColorPower)}" ChoiceCode_="{dictCColorPowerCode.get(controlColorPower)}"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="{dictCControllerDesc.get(controlController)}" ChoiceCode_="{dictCControllerCode.get(controlController)}"/>')

            try:
                # print(blindData.get('torque '))
                # print(blindData.get('reid'))
                torque = float(blindData.get('torque'))
            except:
                return -101

            if(controlClutchMotor == "SG Rechargeable - [SGRM]" or controlClutchMotor == "SG Bi-Directional - [SGRM]"):
                if (torque <= 1.1):
                    resultList.append(
                        f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="SGRM1.1-1.1Nm Sunglow Bi Motor" ChoiceCode_="Y_CLS_SGRMB1"/>')
                elif (torque <= 2):
                    resultList.append(
                        f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="SGRM2-2Nm Sunglow Bi Motor" ChoiceCode_="Y_CLS_SGRMB2"/>')
                # if(controlClutchMotor == "SG Rechargeable Motor" or controlClutchMotor == "SG Bi-Directional - [SGRM]"):
                #     resultList.append(
                #         f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="5V-Battery" ChoiceCode_="Y_CLT_M5"/>')
            else:
                resultList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Clutch Selection' Choice_='{dictClutchMotorDesc.get(controlClutchMotor)}' ChoiceCode_='{dictClutchMotorCode.get(controlClutchMotor)}'/>")

            return resultList

        # Neo
        elif(controlSystem == 'Neo' or controlSystem == 'Chainless'):
            resultList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Control Type' Choice_='{dictNeoDesc.get(neo)}' ChoiceCode_='{dictNeoCode.get(neo)}'/>")
            return resultList

        # Vision
        elif(controlSystem == 'Chain - Vision'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')

            if (controlColorPower == "Stainless Steel"):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="CH-Metal Chain" ChoiceCode_="Y_COP1_CH10"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="CH-Plastic Chain" ChoiceCode_="Y_COP1_PBC"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Chain Color" Choice_="{dictCColorPowerDesc.get(controlColorPower)}" ChoiceCode_="{dictCColorPowerCode.get(controlColorPower)}"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="{dictCControllerDesc.get(controlController)}" ChoiceCode_="{dictCControllerCode.get(controlController)}"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="{dictClutchMotorDesc.get(controlClutchMotor)}" ChoiceCode_="{dictClutchMotorCode.get(controlClutchMotor)}"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-L.A.M." Choice_="{dictVisionDesc.get(spring)}" ChoiceCode_="{dictVisionCode.get(spring)}"/>')

            resultList.extend(self.handleVision(blindData))

            return resultList

        # Diamond
        elif(controlSystem == 'Aria' or controlSystem == 'Diamond'):
            resultList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Control Type' Choice_='NE1\"-Neo 1\"' ChoiceCode_='Y_COP1_1'/>")
            return resultList

        # elif(controlSystem == 'Glydea' or controlSystem == 'GLYDEA-M'):
        #     resultList.append(f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="{dictClutchMotorDesc.get(controlClutchMotor)}" ChoiceCode_="{dictClutchMotorCode.get(controlClutchMotor)}"/>')
        #     return resultList

        else:
            return -102

    def addSBControl(self, blindData):
        controlPosition = blindData.get('controlPosition')
        controlSystem = blindData.get('controlSystem')
        controlColorPower = blindData.get('controlColorPower')
        controlController = blindData.get('controlController')
        controlClutchMotor = blindData.get('controlClutchMotor')
        controlclutchCover = blindData.get('controlclutchCover')
        neo = blindData.get('neo')

        tube = blindData.get('tube')

        shade = blindData.get('shade')

        resultList = [
            f'\n<TEDIOptionList_Details OptionName_="-Control" Choice_="{dictCSystemDesc.get(controlSystem)}" ChoiceCode_="{dictCSystemCode.get(controlSystem)}"/>']

        # Chain
        if(controlSystem == 'Chain'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')

            if (controlColorPower == "Stainless Steel"):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="CH-Metal Chain" ChoiceCode_="Y_COP1_CH10"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="CH-Plastic Chain" ChoiceCode_="Y_COP1_PBC"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Chain Color" Choice_="{dictSBChainColorDesc.get(controlColorPower)}" ChoiceCode_="{dictSBChainColorCode.get(controlColorPower)}"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="{dictSBControllerDesc.get(controlController)}" ChoiceCode_="{dictSBControllerCode.get(controlController)}"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="{dictSBClutchMotorDesc.get(controlClutchMotor)}" ChoiceCode_="{dictSBClutchMotorCode.get(controlClutchMotor)}"/>')

            # TODO Handle Chain may need to be updated?
            # Disabling Handle Chain and letting blind data handle it?
            # resultList.extend(self.handleChain(blindData))

            return resultList

        # Motor
        elif(controlSystem == 'Motor'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')
            if(controlClutchMotor == "SG Rechargeable Motor" or controlClutchMotor == "SG Bi-Directional - [SGRM]"):
                    resultList.append(
                        f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="5V-Battery" ChoiceCode_="Y_CLT_M5"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="{dictSBControllerDesc.get(controlColorPower)}" ChoiceCode_="{dictSBControllerCode.get(controlColorPower)}"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="{dictCControllerDesc.get(controlController)}" ChoiceCode_="{dictCControllerCode.get(controlController)}"/>')

            try:
                # print(blindData.get('torque '))
                # print(blindData.get('reid'))
                torque = float(blindData.get('torque'))
            except:
                return -101

            # Add Line Voltage shape here
            if(controlController == 'Line Voltage'):
                if(controlClutchMotor == 'Sonesse 50 RS485 (10 Nm) - [SSH510485]' or controlClutchMotor == 'Sonesse 50 RS485 (6 Nm) - [SSH506485]' or controlClutchMotor == 'Sonesse 50 RTS (10 Nm) - [SSH510RTS]' or controlClutchMotor == 'Sonesse 50 RTS (6 Nm) - [SSH506RTS]' or controlClutchMotor == 'Sonesse 50 WT (10 Nm) - [SSH510WT]' or controlClutchMotor == 'Sonesse 50 WT (6 Nm) - [SSH506WT]' or controlClutchMotor == 'Sonesse Ultra 50 RS485 (6 Nm) - [SUSH506485]' or controlClutchMotor == 'Sonesse Ultra 50 RTS (6 Nm) - [SUSH506RTS]' or controlClutchMotor == 'Sonesse Ultra 50 WT (6 Nm) - [SUSH506WT]'):
                    resultList.append(
                        f'\n<TEDIOptionList_Details OptionName_="-Clutch/Mot. Head" Choice_="Star-Star" ChoiceCode_="Y_CC_STAR"/>')

                elif(controlClutchMotor == 'Sonesse 50 RTS (10 Nm) - [SRH510RTS]' or controlClutchMotor == 'Sonesse 50 RTS (6 Nm) - [SRH506RTS]' or controlClutchMotor == 'Sonesse 50 WT (10 Nm) - [SRH510WT]' or controlClutchMotor == 'Sonesse 50 WT (6 Nm) - [SRH506WT]' or controlClutchMotor == 'Sonesse Ultra 50 RTS (6 Nm) - [SURH506RTS]' or controlClutchMotor == 'Sonesse Ultra 50 WT (6 Nm) - [SURH506WT]' or controlClutchMotor == 'Sonesse Ultra 50 DC RS485 (4 Nm) - [SU504DC485]' or controlClutchMotor == 'Sonesse Ultra 50 DC RTS (4 Nm) - [SU504DCRTS]'):
                    resultList.append(
                        f'\n<TEDIOptionList_Details OptionName_="-Clutch/Mot. Head" Choice_="Round-Round" ChoiceCode_="Y_CC_ROUND"/>')

            if(controlClutchMotor == "SG Rechargeable Motor" or controlClutchMotor == "SG Bi-Directional - [SGRM]"):
                # if (torque <= 0.7):
                #     resultList.append(
                #         f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="SGRM0.7-0.7Nm Sunglow Bi Motor" ChoiceCode_="Y_CLSSB_SGRMB"/>')
                if (torque <= 1.1):
                    resultList.append(
                        f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="SGRM1.1-1.1Nm Sunglow Bi Motor" ChoiceCode_="Y_CLSSB_SGRMB1"/>')
                elif (torque <= 2):
                    resultList.append(
                        f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="SGRM2-2Nm Sunglow Bi Motor" ChoiceCode_="Y_CLSSB_SGRMB2"/>')
                
        # <TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="12V-Low Voltage" ChoiceCode_="Y_CLT_M12V"/> 
            else:
                resultList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Clutch Selection' Choice_='{dictClutchMotorDesc.get(controlClutchMotor)}' ChoiceCode_='{dictClutchMotorCode.get(controlClutchMotor)}'/>")
                    
                    # f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="{dictSBClutchMotorDesc.get(controlClutchMotor)}" ChoiceCode_="{dictSBClutchMotorCode.get(controlClutchMotor)}"/>')

            return resultList

        elif(controlSystem == 'ZeroGravity'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="ZG-Zero Gravity" ChoiceCode_="Y_CLT_ZG"/>')
            # TO DO ZG01 TO HEAVY MEDIUM LIGHT?
            # Add Spring Assist section here? minin ninin etc?
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Spring Assist" Choice_="{dictZGSpringDesc.get(controlClutchMotor)}" ChoiceCode_="{dictZGSpringCode.get(controlClutchMotor)}"/>')

            # STill need this for mini etc
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="{dictSBClutchMotorDesc.get(controlClutchMotor)}" ChoiceCode_="{dictSBClutchMotorCode.get(controlClutchMotor)}"/>')

            return resultList

        # Neo
        elif(controlSystem == 'Neo' or controlSystem == 'Chainless'):
            resultList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Control Type' Choice_='{dictSBNeoDesc.get(controlClutchMotor)}' ChoiceCode_='{dictSBNeoCode.get(controlClutchMotor)}'/>")
            return resultList

        else:
            return -102

    def addFixedSystem(self, blindData):
        system = blindData.get('controlSystem')
        detail = blindData.get('controlColorPower')
        side = blindData.get('controlController')
        shape = blindData.get('controlClutchMotor')

        resultList = []

        if(system == "Tension Rod"):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName="-Control Option" Choice_="{dictFixedDetailDesc.get(detail)}" ChoiceCode_="{dictFixedDetailCode.get(detail)}"/>')

        elif(system == "Velcro Angle w/ Bottom Bar"):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName="-Arch" Choice_="{dictFixedShapeDesc.get(shape)}" ChoiceCode_="{dictFixedShapeCode.get(shape)}"/>')

        elif(system == "Velcro Panel"):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName="-Velcro Sides" Choice_="{dictFixedSideDesc.get(side)}" ChoiceCode_="{dictFixedSideCode.get(side)}"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName="-Arch" Choice_="{dictFixedShapeDesc.get(shape)}" ChoiceCode_="{dictFixedShapeCode.get(shape)}"/>')

        return resultList

    def addValance(self, blindData):
        resultList = []

        valance = blindData.get('valance')
        valanceFinish = blindData.get('valanceFinish')
        valanceCaps = blindData.get('valanceCaps')
        valanceReturn = blindData.get('valanceReturn')
        endCap = blindData.get('endCap')

        resultList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Valance Type' Choice_='{dictValanceDesc.get(valance)}' ChoiceCode_='{dictValanceCode.get(valance)}'/>")

        # Open Roll
        if (valance == 'Open Roll'):
            resultList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Bracket Color' Choice_='{dictOpenValanceFinishDesc.get(valanceFinish)}' ChoiceCode_='{dictOpenValanceFinishCode.get(valanceFinish)}'/>")
            # No need only one option in BD?

        # Decora
        elif (valance == 'Decora 8' or valance == 'Curved Cassette S'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictD8ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictD8ColorCode.get(valanceFinish)}"/>')
        elif (valance == 'Decora 12' or valance == 'Curved Cassette M'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictD12ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictD12ColorCode.get(valanceFinish)}"/>')
        elif (valance == 'Decora 16' or valance == 'Curved Cassette L'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictD16ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictD16ColorCode.get(valanceFinish)}"/>')

        # SF
        elif (valance == '3" Fascia'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictSF3ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictSF3ColorCode.get(valanceFinish)}"/>')
        elif (valance == '4" Fascia'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictSF4ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictSF4ColorCode.get(valanceFinish)}"/>')
        elif (valance == '5" Fascia'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictSF5ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictSF5ColorCode.get(valanceFinish)}"/>')

        # CBX
        elif (valance == 'CBX'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictCBXColorDesc.get(valanceFinish)}" ChoiceCode_="{dictCBXColorCode.get(valanceFinish)}"/>')

        # HC & HCC
        elif (valance == 'Hanger & Closure w/Brush 4"-5' or valance == 'Hanger & Closure w/Cover & Brush 4"-5"'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="4\"-Hanger & Closure 4\"" ChoiceCode_="Y_VALO_HC4"/>')
        elif (valance == 'Hanger & Closure > 5"' or valance == 'Hanger & Closure w/Cover > 5"'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="5\"-Hanger & Closure 5\"" ChoiceCode_="Y_VALO_HC5"/>')

        elif (valance == 'Hanger & Closure w/Brush 4"-5' or valance == 'Hanger & Closure > 5"'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictHCColorDesc.get(valanceFinish)}" ChoiceCode_="{dictHCColorCode.get(valanceFinish)}"/>')
        elif(valance == 'Hanger & Closure w/Cover & Brush 4"-5"' or valance == 'Hanger & Closure w/Cover > 5"'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictHCCColorDesc.get(valanceFinish)}" ChoiceCode_="{dictHCCColorCode.get(valanceFinish)}"/>')

        # PVC Valance
        elif (valance == 'PVC Valance'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictPVCColorDesc.get(valanceFinish)}" ChoiceCode_="{dictPVCColorCode.get(valanceFinish)}"/>')
            if (valanceReturn != None and valanceReturn != "0"):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="R-With return" ChoiceCode_="Y_VALO_R"/>')

        # Vision
        elif (valance == 'V102 Front & Return Fascia' or valance == 'V102 Front, Return & Back Fascia' or valance == 'V102 Front, Return, Back & Top Fascia'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictV102ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictV102ColorCode.get(valanceFinish)}"/>')

        elif (valance == 'V84 Front & Return Fascia' or valance == 'V84 Front, Return & Back Fascia' or valance == 'V84 Front, Return, Back & Top Fascia'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictV84ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictV84ColorCode.get(valanceFinish)}"/>')

        # Aria
        # TODO Currently fixed to white as default
        elif (valance == 'Aria' or valance == 'Diamond'):
            # valanceFinishDesc = f'{valanceFinish} , "WH(AR)-WH"'
            # valanceFinishCode = f'{valanceFinish} , "Y_AR_W"'

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictAriaColorDesc.get(valanceFinish)}" ChoiceCode_="{dictAriaColorCode.get(valanceFinish)}"/>')

            # resultList.append(
            #     f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="WH(AR)-White" ChoiceCode_="Y_AR_W"/>')

        # OTHER
        # if (valance != 'Open Roll' and valance != 'Fabric Valance'):
        #     resultList.append(f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictValanceFinishDesc.get(valanceFinish)}" ChoiceCode_="{dictValanceFinishCode.get(valanceFinish)}"/>')

        if (valanceCaps != None and valanceCaps != "None"):
            if((valance != '3" Fascia' and valance != '4" Fascia' and valance != '5" Fascia') or endCap == True):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictValanceCapsCode.get(valanceCaps)}"/>')

        # Fabric Valance Return
        if(valance == 'Fabric Valance'):
            if (valanceReturn != None and valanceReturn != "0"):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="R-With return" ChoiceCode_="Y_VALO_R"/>')

        return resultList

    def addSBValance(self, blindData):
        resultList = []

        controlSystem = blindData.get('controlSystem')
        valance = blindData.get('valance')
        valanceFinish = blindData.get('valanceFinish')
        valanceCaps = blindData.get('valanceCaps')
        valanceReturn = blindData.get('valanceReturn')
        endCap = blindData.get('endCap')

        # TODO Fabric Valance has issues regarding in/out mount and drops
        if(valance == 'Fabric Valance'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="IM-Inside Mount" ChoiceCode_="Y_VALO_IM"/>')

            if(valanceFinish == '6 Inch Drop'):
                resultList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Valance Type' Choice_='{dictValanceDesc.get('Fabric Valance 6')}' ChoiceCode_='{dictValanceCode.get('Fabric Valance 6')}'/>")
            elif(valanceFinish == '8 Inch Drop'):
                resultList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Valance Type' Choice_='{dictValanceDesc.get('Fabric Valance 8')}' ChoiceCode_='{dictValanceCode.get('Fabric Valance 8')}'/>")

        elif (valance == 'Fabric Valance w/ Return'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="OM-Outside Mount" ChoiceCode_="Y_VALO_OM"/>')

            if(valanceFinish == '6 Inch Drop'):
                resultList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Valance Type' Choice_='{dictValanceDesc.get('Fabric Valance 6')}' ChoiceCode_='{dictValanceCode.get('Fabric Valance 6')}'/>")
            elif(valanceFinish == '8 Inch Drop'):
                resultList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Valance Type' Choice_='{dictValanceDesc.get('Fabric Valance 8')}' ChoiceCode_='{dictValanceCode.get('Fabric Valance 8')}'/>")

        else:
            if(valance == 'Open Roll' and controlSystem == 'Neo'):
                resultList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Valance Type' Choice_='ORN-No valance Neo' ChoiceCode_='Y_VALT_NEO'/>")
            else:
                resultList.append(
                    f"\n<TEDIOptionList_Details OptionName_='-Valance Type' Choice_='{dictValanceDesc.get(valance)}' ChoiceCode_='{dictValanceCode.get(valance)}'/>")

        # Open Roll
        if (valance == 'Open Roll'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="NA(OR)-OR" ChoiceCode_="Y_OR_NA"/>')

            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Bracket Color" Choice_="{dictSBBracketColorDesc.get(valanceFinish)}" ChoiceCode_="{dictSBBracketColorCode.get(valanceFinish)}"/>')

            if(endCap == 'Yes'):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceFinish)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceFinish)}"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_=".-N/A" ChoiceCode_="Y_BRKV_N"/>')

        # Decora
        elif (valance == 'SB Compact Curved Cassette'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictCCCColorDesc.get(valanceFinish)}" ChoiceCode_="{dictCCCColorCode.get(valanceFinish)}"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceCaps)}"/>')

        elif (valance == 'SB Wrapped Compact Curved Cassette'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictCCCWColorDesc.get(valanceFinish)}" ChoiceCode_="{dictCCCWColorCode.get(valanceFinish)}"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceCaps)}"/>')

        elif (valance == 'SB Curved Cassette'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictCCColorDesc.get(valanceFinish)}" ChoiceCode_="{dictCCColorCode.get(valanceFinish)}"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceCaps)}"/>')

        elif (valance == 'SB Wrapped Curved Cassette'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictCCWColorDesc.get(valanceFinish)}" ChoiceCode_="{dictCCWColorCode.get(valanceFinish)}"/>')
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceCaps)}"/>')

        # SF
        elif (valance == 'SB 3" Fascia'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictSQF3ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictSQF3ColorCode.get(valanceFinish)}"/>')
            if(endCap == 'Yes'):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceCaps)}"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_=".-N/A" ChoiceCode_="Y_BRKV_N"/>')

        elif (valance == 'SB 4" Fascia'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictSQF4ColorDesc.get(valanceFinish)}" ChoiceCode_="{dictSQF4ColorCode.get(valanceFinish)}"/>')
            if(endCap == 'Yes'):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceCaps)}"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_=".-N/A" ChoiceCode_="Y_BRKV_N"/>')

        elif (valance == 'SB 4" Wrapped Fascia'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictSQF4WColorDesc.get(valanceFinish)}" ChoiceCode_="{dictSQF4WColorCode.get(valanceFinish)}"/>')
            if(endCap == 'Yes'):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceCaps)}"/>')
            else:
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_=".-N/A" ChoiceCode_="Y_BRKV_N"/>')

        # PVC Valance
        elif (valance == 'PVC Valance'):
            resultList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Finish" Choice_="{dictPVCColorDesc.get(valanceFinish)}" ChoiceCode_="{dictPVCColorCode.get(valanceFinish)}"/>')
            if (valanceReturn != None and valanceReturn != "0"):
                resultList.append(
                    f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="R-With return" ChoiceCode_="Y_VALO_R"/>')

        # Moving Caps to the fascia/decoras, without the valance caps check, it should work...
        # if (valanceCaps != None and valanceCaps != "None" and valance != 'Open Roll'):
        #     if((valance != 'SB 3" Fascia' and valance != 'SB 4" Fascia' and valance != 'SB 4" Wrapped Fascia' and valance != 'Fabric Valance' and valance != 'Fabric Valance w/ Return') or endCap == 'Yes'):
        #         resultList.append(f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_="{dictSBValanceCapsDesc.get(valanceCaps)}" ChoiceCode_="{dictSBValanceCapsCode.get(valanceCaps)}"/>')
        #     else:
        #         resultList.append(f'\n<TEDIOptionList_Details OptionName_="-Bracket Cover" Choice_=".-N/A" ChoiceCode_="Y_BRKV_N"/>')

        # TODO Fabric Valance has issues regarding in/out mount and drops
        # May have to use inside/outside mount to do return or not
        # Fabric Valance Return
        # if(valance == 'Fabric Valance'):
        #     if (valanceReturn != None and valanceReturn != "0"):
        #         resultList.append(f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="R-With return" ChoiceCode_="Y_VALO_R"/>')

        return resultList

    def addVision(self, blindData):
        returnList = []

        valance = blindData.get('valance')

        if (valance == 'V84 Front & Return Fascia'):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="FR-Front & Return 84" ChoiceCode_="Y_VALO_VFR84"/>')

        elif (valance == 'V84 Front, Return & Back Fascia'):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="FRB-Front Return & Back" ChoiceCode_="Y_VALO_84FRB"/>')

        elif (valance == 'V84 Front, Return, Back & Top Fascia'):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="FRB-Front Return & Back" ChoiceCode_="Y_VALO_84FRB"/>')
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Top Cover" Choice_="T-With Top cover 84" ChoiceCode_="Y_VALO_VT84"/>')

        elif (valance == 'V102 Front & Return Fascia'):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="FR-Front & Return 102" ChoiceCode_="Y_VALO_VFR102"/>')

        elif (valance == 'V102 Front, Return & Back Fascia'):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="FRB-Front Return & Back" ChoiceCode_="Y_VALO_102FRB"/>')

        elif (valance == 'V102 Front, Return, Back & Top Fascia'):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Valance Option" Choice_="FRB-Front Return & Back" ChoiceCode_="Y_VALO_102FRB"/>')
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Top Cover" Choice_="T-With top cover 102" ChoiceCode_="Y_VALO_VT102"/>')

        return returnList

    def addTrimPull(self, blindData):
        returnList = []

        if(blindData.get('trim') != None):
            trim = blindData.get('trim').lower()
            trimVar = trim + " " + blindData.get('trimColor').lower()
            if(trim != None and trim != 'none' and trim != ''):
                print(trimVar)
                returnList.append(
                    f'\n<TEDIOptionList_Details OptionName="-Trims" Choice_="{dictTrimsDesc.get(trimVar)}" ChoiceCode_="{dictTrimsCode.get(trimVar)}"/>')

        if(blindData.get('pull') != None):
            pull = blindData.get('pull').lower()
            pullVar = pull + " " + blindData.get('pullColor').lower()
            if(pull != None and pull != 'none' and pull != ''):
                returnList.append(
                    f'\n<TEDIOptionList_Details OptionName="-Pull" Choice_="{dictPullsDesc.get(pullVar)}" ChoiceCode_="{dictPullsCode.get(pullVar)}"/>')

        return returnList

    def addLAM(self, blindData):
        returnList = []

        lam = blindData.get('liftAssist')
        ultra = blindData.get('ultraLite')
        springAssist = blindData.get('springAssist')
        tube = blindData.get('tube')

        if (lam == "true"):
            # if (ultra == "true" and tube == '1 1/2'):
            if (ultra == "true" and tube != "2" and tube != "2 1/2"):
                returnList.append(
                    f'\n<TEDIOptionList_Details OptionName="-Spring Assist" Choice_="LAM-Lift Assist Mechanism" ChoiceCode_="Y_SA_Y"/>')
                returnList.append(
                    f'\n<TEDIOptionList_Details OptionName="-L.A.M." Choice_="UL-Ultra Lite" ChoiceCode_="Y_SPOP_UL"/>')
            # elif (springAssist == "true" and (tube == '2' or tube == '2 1/2') ):
            elif (springAssist == "true"):
                returnList.append(
                    f'\n<TEDIOptionList_Details OptionName="-Spring Assist" Choice_="LAM-Lift Assist Mechanism" ChoiceCode_="Y_SA_Y"/>')
                returnList.append(
                    f'\n<TEDIOptionList_Details OptionName="-L.A.M." Choice_="SA-Spring Assist" ChoiceCode_="Y_SPOP_SA"/>')

        return returnList

    def addSBLAM(self, blindData):
        returnList = []

        lam = blindData.get('liftAssist')
        spring = blindData.get('spring')

        if (lam == "true"):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName="-L.A.M." Choice_="SA-Spring Assist" ChoiceCode_="Y_SPOP_SA"/>')
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Spring Assist" Choice_="{dictSpringDesc.get(spring)}" ChoiceCode_="{dictSpringCode.get(spring)}"/>')

        return returnList

    def addClutchColor(self, blindData):
        returnList = []
        color = blindData.get('clutchColor')
        if (color != None and color != "None" and color != ""):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName="-Clutch/Mot. Head" Choice_="{dictClutchColorDesc.get(color)}" ChoiceCode_="{dictClutchColorCode.get(color)}"/>')

        return returnList

    def addChildSafety(self, blindData):
        returnList = []

        safety = blindData.get('childSafety')
        controlSystem = blindData.get('controlSystem')

        if (controlSystem == 'Chain' or controlSystem == 'Cord' or controlSystem == 'Chain - Vision'):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName="-Chain Hold down" Choice_="{dictChildSafetyDesc.get(safety)}" ChoiceCode_="{dictChildSafetyCode.get(safety)}"/>')

        return returnList

    def addHoldDown(self, blindData):
        returnList = []
        holdDown = blindData.get('holdDownBrackets')

        if (holdDown == "true"):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName="-Hem Hold down" Choice_="HDB-Hold Down Bracket" ChoiceCode_="Y_HDB_Y"/>')

        return returnList

    def addSideChannels(self, blindData):
        returnList = []
        sC = blindData.get('sideChannel')
        sCMount = blindData.get('sideChannelMount')
        sCFinish = blindData.get('sideChannelFinish')

        if (sC != None and sC != "None" and sC != ''):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName="-Side Ch. Type" Choice_="{dictSideChannelDesc.get(sC)}" ChoiceCode_="{dictSideChannelCode.get(sC)}"/>')
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName="-SCMount" Choice_="{dictSCMountDesc.get(sCMount)}" ChoiceCode_="{dictSCMountCode.get(sCMount)}"/>')
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName="-Side Ch. Finish" Choice_="{dictSCColorDesc.get(sCFinish)}" ChoiceCode_="{dictSCColorCode.get(sCFinish)}"/>')

        return returnList

    def addRollType(self, blindData):
        returnList = []
        rollType = blindData.get('rollType')
        if (rollType != None):
            returnList.append(
                f'\n<TEDIOptionList_Details OptionName="-Shade Rolling" Choice_="{dictRollTypeDesc.get(rollType)}" ChoiceCode_="{dictRollTypeCode.get(rollType)}"/>')
        return returnList

    def addPanelOptions(self, blindData):
        returnList = []

        shade = blindData.get('shade')
        channel = blindData.get('channel')
        stationary = blindData.get('stationary')
        panOpen = blindData.get('open')

        if(shade == "PANEL TRACK"):
            returnList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Channels' Choice_='{dictChannelDesc.get(channel)}'  ChoiceCode_='{dictChannelCode.get(channel)}'/>")

            returnList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Panel Opt. 1' Choice_='{dictStationaryDesc.get(stationary)}'  ChoiceCode_='{dictStationaryCode.get(stationary)}'/>")

            returnList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Stack' Choice_='{dictOpenDesc.get(panOpen)}'  ChoiceCode_='{dictOpenCode.get(panOpen)}'/>")

        return returnList

    def productDetails(self, blindData):
        code = blindData.get('code')
        quantity = blindData.get('quantity')

        location = blindData.get('shadeID', 'Missing Location')
        orderID = blindData.get('PO')

        returnList = [
            '\n\n<TEDIOrderDetails_Details',
            '\nBlindTypeDescription_="Miscellaneous"',
            '\nBlindTypeCode_="M"', '\nMeasureName_="F-Finish"',
            '\nMetricMeasurement_="1" \nWidth_="0" \nDrop_="0" \nWidthDisplay_="0" \nDropDisplay_="0"',
            '\nUnitOfSaleDescription_="PC"',
            f"\nOrderDetailComment_='{dictAddDesc.get(code)}'",
            f'\nFullQuantity_="{quantity}"',
            f'\nFabricCode_="{dictAddCode.get(code)}"',
            f"\nFabricDescription_='{dictAddDesc.get(code)}'",
            f'\nLocation_=""',
            f'\nQuantity_="{quantity}"',
            f'\nOrderID_="{orderID}"',
            '\nIsDetailTwoDayDespatch_="FALSE">',
            '\n</TEDIOrderDetails_Details>']

        return returnList

    def rollerDetails(self, blindData):

        tube = blindData.get('tube')
        mount = blindData.get('mount')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')
        # Tube
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Tube' Choice_='{dictTubeDesc.get(tube)}'  ChoiceCode_='{dictTubeCode.get(tube)}'/>")

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addValance(blindData))

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')

        # Advanced Options
        shadeList.extend(self.addTrimPull(blindData))
        shadeList.extend(self.addLAM(blindData))
        shadeList.extend(self.addClutchColor(blindData))
        shadeList.extend(self.addChildSafety(blindData))
        shadeList.extend(self.addHoldDown(blindData))
        shadeList.extend(self.addSideChannels(blindData))
        shadeList.extend(self.addRollType(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def interludeDetails(self, blindData):

        tube = blindData.get('tube')
        mount = blindData.get('mount')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')
        # Tube
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Tube' Choice_='{dictTubeDesc.get(tube)}'  ChoiceCode_='{dictTubeCode.get(tube)}'/>")

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addValance(blindData))

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')

        # Advanced Options
        shadeList.extend(self.addChildSafety(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def illusionDetails(self, blindData):

        tube = blindData.get('tube')
        mount = blindData.get('mount')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')
        # Tube
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Tube' Choice_='{dictTubeDesc.get(tube)}'  ChoiceCode_='{dictTubeCode.get(tube)}'/>")

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addValance(blindData))

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')

        # Advanced Options
        shadeList.extend(self.addChildSafety(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def fixedDetails(self, blindData):
        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        shadeList.extend(self.addFixedSystem(blindData))

        # Advanced Options
        shadeList.extend(self.addTrimPull(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def visionDetails(self, blindData):
        tube = blindData.get('tube')
        mount = blindData.get('mount')
        valance = blindData.get('valance')
        endCaps = blindData.get('endCap')
        railroad = blindData.get('railroad')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        # Railroad
        if(railroad == 'true'):
            shadeList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Railroad' Choice_='RR-Railroad'  ChoiceCode_='Y_RR_Y'/>")

        # Tube
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Tube' Choice_='{dictTubeDesc.get(tube)}'  ChoiceCode_='{dictTubeCode.get(tube)}'/>")

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addValance(blindData))
        shadeList.extend(self.addVision(blindData))

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')
        if((valance == 'V84 Front & Return Fascia' or valance == 'V84 Front, Return & Back Fascia' or valance == 'V84 Front, Return, Back & Top Fascia') and endCaps == 'Flexible'):
            shadeList.append(
                f'\n<TEDIOptionList_Details OptionName_="-Mounting Bracket" Choice_="V84-Flex Mounting Bracket" ChoiceCode_="Y_FMBT_V84"/>')

        # Advanced Options
        shadeList.extend(self.addTrimPull(blindData))
        shadeList.extend(self.addChildSafety(blindData))
        shadeList.extend(self.addSideChannels(blindData))
        shadeList.extend(self.addRollType(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def romanDetails(self, blindData):
        shadeList = []
        mount = blindData.get('mount')

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')

        # Advanced Options
        shadeList.extend(self.addChildSafety(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def ariaDetails(self, blindData):
        mount = blindData.get('mount')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addValance(blindData))

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def panelDetails(self, blindData):
        mount = blindData.get('mount')
        railroad = blindData.get('railroad')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        # Railroad
        if(railroad == 'true'):
            shadeList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Railroad' Choice_='RR-Railroad'  ChoiceCode_='Y_RR_Y'/>")

        # Panel Options
        shadeList.extend(self.addPanelOptions(blindData))

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addValance(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def sbRollerDetails(self, blindData):
        tube = blindData.get('tube')
        mount = blindData.get('mount')
        controlSystem = blindData.get('controlSystem')
        railroad = blindData.get('railroad')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        # Railroad
        if(railroad == 'true'):
            shadeList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Railroad' Choice_='RR-Railroad'  ChoiceCode_='Y_RR_Y'/>")

        # Tube
        if(controlSystem == 'Neo' or controlSystem == 'Chainless'):
            shadeList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Tube' Choice_='W(38mm)1.5-W1.5'  ChoiceCode_='Y_TTSB_1.5W'/>")
        else:
            shadeList.append(
                f"\n<TEDIOptionList_Details OptionName_='-Tube' Choice_='{dictSBTubeDesc.get(tube)}'  ChoiceCode_='{dictSBTubeCode.get(tube)}'/>")

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addSBControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addSBValance(blindData))

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')

        # Advanced Options
        shadeList.extend(self.addTrimPull(blindData))
        shadeList.extend(self.addSBLAM(blindData))
        shadeList.extend(self.addClutchColor(blindData))
        shadeList.extend(self.addChildSafety(blindData))
        shadeList.extend(self.addHoldDown(blindData))
        shadeList.extend(self.addSideChannels(blindData))
        shadeList.extend(self.addRollType(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def sbIntDetails(self, blindData):
        tube = blindData.get('tube')
        mount = blindData.get('mount')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        # Tube
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Tube' Choice_='{dictSBTubeDesc.get(tube)}'  ChoiceCode_='{dictSBTubeCode.get(tube)}'/>")

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addSBControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addSBValance(blindData))

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')

        # Advanced Options
        shadeList.extend(self.addClutchColor(blindData))
        shadeList.extend(self.addChildSafety(blindData))
        shadeList.extend(self.addHoldDown(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def sbIllDetails(self, blindData):
        tube = blindData.get('tube')
        mount = blindData.get('mount')

        shadeList = []

        # Details, Fabric
        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        # Tube
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Tube' Choice_='{dictSBTubeDesc.get(tube)}'  ChoiceCode_='{dictSBTubeCode.get(tube)}'/>")

        # Hem
        shadeList.extend(self.addHem(blindData))

        # Control
        control = self.addSBControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        # Valance
        shadeList.extend(self.addSBValance(blindData))

        # Mount
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')

        # Advanced Options
        shadeList.extend(self.addClutchColor(blindData))
        shadeList.extend(self.addChildSafety(blindData))
        shadeList.extend(self.addHoldDown(blindData))

        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def addGlydeaControl(self, blindData):
        controlPosition = blindData.get('controlPosition')
        controlSystem = blindData.get('controlSystem')
        controlColorPower = blindData.get('controlColorPower')
        controlController = blindData.get('controlController')
        controlClutchMotor = blindData.get('controlClutchMotor')

        controlList = []

        controlList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Control Drive" Choice_="{dictCPositionDesc.get(controlPosition)}" ChoiceCode_="{dictCPositionCode.get(controlPosition)}"/>')
        controlList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Clutch/Motor Type" Choice_="{dictCColorPowerDesc.get(controlColorPower)}" ChoiceCode_="{dictCColorPowerCode.get(controlColorPower)}"/>')
        controlList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Control Type" Choice_="{dictCControllerDesc.get(controlController)}" ChoiceCode_="{dictCControllerCode.get(controlController)}"/>')
        controlList.append = (
            f'\n<TEDIOptionList_Details OptionName_="-Control" Choice_="{dictCSystemDesc.get(controlSystem)}" ChoiceCode_="{dictCSystemCode.get(controlSystem)}"/>')
        controlList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Clutch Selection" Choice_="{dictClutchMotorDesc.get(controlClutchMotor)}" ChoiceCode_="{dictClutchMotorCode.get(controlClutchMotor)}"/>')

        return controlList

    def glydeaDetails(self, blindData):
        panOpen = blindData.get('open')
        armType = blindData.get('track')
        carrierType = blindData.get('drapery')
        pulley = blindData.get('idle')
        mount = blindData.get('mount')
        shadeList = []

        shadeList.extend(self.blindDetails(blindData))
        shadeList.append('\n')

        control = self.addGlydeaControl(blindData)
        if(isinstance(control, list)):
            shadeList.extend(control)
        else:
            return control

        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Stack' Choice_='{dictOpenDesc.get(panOpen)}'  ChoiceCode_='{dictOpenCode.get(panOpen)}'/>")
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Arm Type' Choice_='{dictArmTypeDesc.get(armType)}'  ChoiceCode_='{dictArmTypeCode.get(armType)}'/>")
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Carrier Type' Choice_='{dictCarrierTypeDesc.get(carrierType)}'  ChoiceCode_='{dictCarrierTypeCode.get(carrierType)}'/>")
        shadeList.append(
            f"\n<TEDIOptionList_Details OptionName_='-Pulley' Choice_='{dictPulleyDesc.get(pulley)}'  ChoiceCode_='{dictPulleyCode.get(pulley)}'/>")
        shadeList.append(
            f'\n<TEDIOptionList_Details OptionName_="-Mount" Choice_="{dictMountDesc.get(mount)}" ChoiceCode_="{dictMountCode.get(mount)}"/>')
        shadeList.append(f'\n</TEDIOrderDetails_Details>')

        return shadeList

    def invalidDetails(self, blindData):
        print('Invalid Details')
        return (-103)

    def addDetails(self, blindData):
        switcher = {
            'ROLLER SHADE': self.rollerDetails,
            'INTERLUDE SHADE': self.interludeDetails,
            'ILLUSION SHADE': self.illusionDetails,
            'VISION SHADE': self.visionDetails,
            'FIXED SHADE': self.fixedDetails,
            'ROMAN SHADE': self.romanDetails,
            'PANEL TRACK': self.panelDetails,
            'ARIA SHADE': self.ariaDetails,
            'PRODUCT': self.productDetails,
            'SB ROLLER SHADE': self.sbRollerDetails,
            'SB INTERLUDE SHADE': self.sbIntDetails,
            'SB ILLUSION SHADE': self.sbIllDetails,
            'DRAPERY TRACK': self.glydeaDetails,
            # 'GEMINI DUAL SHADE': self.geminiDetails,
        }

        # Get the function from switcher dictionaryQ
        shade = blindData.get('shade')
        product = blindData.get('product')

        if(shade == 'SB BANDED SHADE'):
            blindData['shade'] = 'SB INTERLUDE SHADE'
            shade = 'SB INTERLUDE SHADE'

        if(shade == 'SB ZEBRA SHADE'):
            blindData['shade'] = 'SB INTERLUDE SHADE'
            shade = 'SB INTERLUDE SHADE'

        if(shade == 'SB SHEER SHADE'):
            blindData['shade'] = 'SB ILLUSION SHADE'
            shade = 'SB ILLUSION SHADE'

        if(shade == 'DIAMOND SHADE'):
            blindData['shade'] = 'ARIA SHADE'
            shade = 'ARIA SHADE'

        if(shade == 'DIAMOND SHADE'):
            blindData['shade'] = 'ARIA SHADE'
            shade = 'ARIA SHADE'

        argument = shade if shade != None else 'PRODUCT'

        # Get the correct blind type, else return Invalid blind
        func = switcher.get(argument, self.invalidDetails)
        # Execute the function
        return func(blindData)

    def makeOrder(self, orderArray, orderHeader):
        # OrderArray is an Array of Orders with SubArrays of Blinds

        stringList = ['<Transfer>']
        if(len(orderArray) == 0):
            return [-104, 'No Orders Selected']

        for order in orderArray:
            # self.stringList.append(order[0].get('email'))
            email = order[0].get('email')
            orderTag = order[0].get('orderTag')
            PO = order[0].get('PO')
            # print(PO)

            # print(f"Generating Order - PO: {PO} - Order Tag: {orderTag} - eMail: {email}")

            genLogger.log(
                f"Attempting PO: {PO} - Order Tag: {orderTag} - eMail: {email}")

            # Select the right order from the OrderTag List, Account Info Here, Delivery Addition Here
            for orderDetails in orderHeader:
                if PO == orderDetails.get('PO'):
                    self.currentOrder = orderDetails

            companyCode = self.currentOrder.get('accountCode')
            companyName = self.currentOrder.get('accountName')

            self.date = datetime.date.today().strftime("%m/%d/%y")
            self.time = datetime.datetime.now().strftime("%I:%M:%S")

            if(companyCode != None):
                stringList.append(
                    f'\n\n<TEDISenderInformation_Details CompanyName_="{companyName}" CompAccCode_="{companyCode}" FileTransfName_="EDITransaction.xml" CreateDate_="{str(self.date)}" CreateTime_="{str(self.time)}">')
            else:
                stringList.append(
                    f'\n\n<TEDISenderInformation_Details CompanyName_="{accountsDesc.get(email, "Sun Glow Window Covering Products of Canada Ltd.")}" CompAccCode_="{accountsCode.get(email, "10376C")}" FileTransfName_="EDITransaction.xml" CreateDate_="{str(self.date)}" CreateTime_="{str(self.time)}">')

            stringList.append(f'\n<TEDIOrderHeader_Details')
            stringList.append(f'\nCustomerReference_="{orderTag}"')
            stringList.append(f'\nOrderDate_="{str(self.date)}"')
            stringList.append(
                f'\nRequiredDate_="{(datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%m/%d/%y")}">')

            # stringList.append(">")

            # Add Blind Details now
            for blind in order:
                # print(blind.get('trim'))
                details = self.addDetails(blind)

                if (isinstance(details, list)):
                    stringList.extend(self.addDetails(blind))
                else:
                    po = blind.get('PO')
                    tag = blind.get('orderTag')
                    orderError = f'Error Processing PO: {po}, Order Tag: {tag}. Error Code: {details}'
                    return [details, orderError]

                # print(self.addDetails(blind))
            stringList.append(f'\n</TEDIOrderHeader_Details>')
            stringList.append(f'\n</TEDISenderInformation_Details>\n')

        # End For
        stringList.append(f'\n</Transfer>')

        # strConcat = " ".join(stringList)

        # print(self.stringList)
        # print(strConcat)
        # print('\n')
        return stringList
