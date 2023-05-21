DIO_Interface='''

/*************************************************************************/
/*************************Interfacing macros******************************/
/*************************************************************************/

/*Possible port IDs*/
#define DIO_PORTA              0
#define DIO_PORTB              1
#define DIO_PORTC              2
#define DIO_PORTD              3

/*Possible pin number*/
#define DIO_PIN0               0
#define DIO_PIN1               1
#define DIO_PIN2               2
#define DIO_PIN3               3
#define DIO_PIN4               4
#define DIO_PIN5               5
#define DIO_PIN6               6
#define DIO_PIN7               7

/*Possible pins directions*/
#define DIO_PIN_OUTPUT         0
#define DIO_PIN_INPUT_FLOAT    1
#define DIO_PIN_INPUT_PULLUP   2

/*possible output pins values*/
#define DIO_LOW_PIN            0
#define DIO_HIGH_PIN           1

/*Possible ports directions*/
#define DIO_PORT_OUTPUT         0
#define DIO_PORT_INPUT_FLOAT    1
#define DIO_PORT_INPUT_PULLUP   2

/*possible output ports values*/
#define DIO_LOW_PORT           0
#define DIO_HIGH_PORT          1


/*************************************************************************/
/*************************Functions' prototypes****************************/
/*************************************************************************/

/*this function shall set the direction of a specific pin*/
void DIO_voidSetPinDirection(u8 Copy_u8PortID , u8 Copy_u8Pin , u8 Copy_u8PinDirection);

/*this function shall set the value of any output pin*/
void DIO_voidSetPinValue(u8 Copy_u8PortID , u8 Copy_u8Pin , u8 Copy_u8PinValue);

/*this function is to set the direction of a specific port*/
void DIO_voidSetPortDirection(u8 Copy_u8PortID  , u8 Copy_u8PortDirection);

/*this function is to set the value of a specific OutPut port*/
/*Return : Error State
 * port value : (0~255)*/
u8 DIO_u8SetPortValue(u8 Copy_u8PortID  , u8 Copy_u8PortValue);

/*this function is to toggle the pin value*/
void DIO_voidTogglePin(u8 Copy_u8PortID , u8 Copy_u8Pin);

/*this function is to get the value of an input pin*/
u8 DIO_u8GetPinValue(u8 Copy_u8PortID , u8 Copy_u8Pin);

'''

DIO_Configuration='''



'''

DIO_Private='''

/*PORT A registers*/
#define PORTA             (*(u8 *)(0x3B))
#define DDRA              (*(u8 *)(0x3A))
#define PINA              (*(u8 *)(0x39))

/*PORT B registers*/
#define PORTB             (*(u8 *)(0x38))
#define DDRB              (*(u8 *)(0x37))
#define PINB              (*(u8 *)(0x36))

/*PORT C registers*/
#define PORTC             (*(u8 *)(0x35))
#define DDRC              (*(u8 *)(0x34))
#define PINC              (*(u8 *)(0x33))

/*PORT D registers*/
#define PORTD             (*(u8 *)(0x32))
#define DDRD              (*(u8 *)(0x31))
#define PIND              (*(u8 *)(0x30))

'''

DIO_Program='''

#include "../../LIB/LIB_STD_TYPES.h"
#include "../../LIB/LIB_BIT_MATH.h"

#include "DIO_private.h"
#include "DIO_interface.h"


/******************************************************************************/
/*************************Functions' implementation****************************/
/******************************************************************************/

void DIO_voidSetPinDirection(u8 Copy_u8PortID , u8 Copy_u8Pin , u8 Copy_u8PinDirection)
{
	/*switching over ports*/
	switch(Copy_u8PortID)
	{
		/*in case of setting the direction of a pin in port A*/
		case DIO_PORTA :

			/*switch over different directions*/
			switch(Copy_u8PinDirection)
			{
				/*in case of setting the pin direction to be output*/
				case DIO_PIN_OUTPUT :
					SET_BIT(DDRA , Copy_u8Pin);
					break ;

				/*in case of setting the pin direction to be input float*/
				case DIO_PIN_INPUT_FLOAT :
					CLR_BIT(DDRA , Copy_u8Pin);
					CLR_BIT(PORTA , Copy_u8Pin);
					break ;

				/*in case of setting the pin direction to be input pull up*/
				case DIO_PIN_INPUT_PULLUP :
					CLR_BIT(DDRA , Copy_u8Pin);
					SET_BIT(PORTA , Copy_u8Pin);
					break ;
			}
			break ;

		/*in case of setting the direction of a pin in port B*/
		case DIO_PORTB :

			/*switch over different directions*/
			switch(Copy_u8PinDirection)
			{
				/*in case of setting the pin direction to be output*/
				case DIO_PIN_OUTPUT :
					SET_BIT(DDRB , Copy_u8Pin);
					break ;

				/*in case of setting the pin direction to be input float*/
				case DIO_PIN_INPUT_FLOAT :
					CLR_BIT(DDRB , Copy_u8Pin);
					CLR_BIT(PORTB , Copy_u8Pin);
					break ;

				/*in case of setting the pin direction to be input pull up*/
				case DIO_PIN_INPUT_PULLUP :
					CLR_BIT(DDRB , Copy_u8Pin);
					SET_BIT(PORTB , Copy_u8Pin);
					break ;
			}
			break ;

		/*in case of setting the direction of a pin in port C*/
		case DIO_PORTC :

			/*switch over different directions*/
			switch(Copy_u8PinDirection)
			{
				/*in case of setting the pin direction to be output*/
				case DIO_PIN_OUTPUT :
					SET_BIT(DDRC , Copy_u8Pin);
					break ;

				/*in case of setting the pin direction to be input float*/
				case DIO_PIN_INPUT_FLOAT :
					CLR_BIT(DDRC , Copy_u8Pin);
					CLR_BIT(PORTC , Copy_u8Pin);
					break ;

				/*in case of setting the pin direction to be input pull up*/
				case DIO_PIN_INPUT_PULLUP :
					CLR_BIT(DDRC , Copy_u8Pin);
					SET_BIT(PORTC , Copy_u8Pin);
					break ;
			}
			break ;

		/*in case of setting the direction of a pin in port D*/
		case DIO_PORTD :

			/*switch over different directions*/
			switch(Copy_u8PinDirection)
			{
				/*in case of setting the pin direction to be output*/
				case DIO_PIN_OUTPUT :
					SET_BIT(DDRD , Copy_u8Pin);
					break ;

				/*in case of setting the pin direction to be input float*/
				case DIO_PIN_INPUT_FLOAT :
					CLR_BIT(DDRD , Copy_u8Pin);
					CLR_BIT(PORTD , Copy_u8Pin);
					break ;

				/*in case of setting the pin direction to be input pull up*/
				case DIO_PIN_INPUT_PULLUP :
					CLR_BIT(DDRD , Copy_u8Pin);
					SET_BIT(PORTD , Copy_u8Pin);
					break ;
			}
			break ;
	}
}

/****************************************************************************************************/
/****************************************************************************************************/

void DIO_voidSetPinValue(u8 Copy_u8PortID , u8 Copy_u8Pin , u8 Copy_u8PinValue)
{
	    /*switching over ports*/
		switch(Copy_u8PortID)
		{
			/*in case of setting the Value of a pin in port A*/
			case DIO_PORTA :
				WRT_BIT(PORTA , Copy_u8Pin , Copy_u8PinValue);
				break ;

			/*in case of setting the Value of a pin in port B*/
			case DIO_PORTB :
				WRT_BIT(PORTB , Copy_u8Pin , Copy_u8PinValue);
				break ;

			/*in case of setting the Value of a pin in port C*/
			case DIO_PORTC :
				WRT_BIT(PORTC , Copy_u8Pin , Copy_u8PinValue);
				break ;

			/*in case of setting the Value of a pin in port D*/
			case DIO_PORTD :
				WRT_BIT(PORTD , Copy_u8Pin , Copy_u8PinValue);
				break ;
		}
}

/****************************************************************************************************/
/****************************************************************************************************/

void DIO_voidSetPortDirection(u8 Copy_u8PortID  , u8 Copy_u8PortDirection)
{
	/*switching over ports*/
	switch(Copy_u8PortID)
	{
		/*in case of setting the direction of port A*/
		case DIO_PORTA :

			/*switch over different directions*/
			switch(Copy_u8PortDirection)
			{
				/*in case of setting the Port to be output*/
				case DIO_PORT_OUTPUT :
					DDRA = 0xff;
					break ;

				/*in case of setting the Port to be input float*/
				case DIO_PORT_INPUT_FLOAT :
					DDRA = 0;
					PORTA = 0;
					break ;

				/*in case of setting the Port to be input pull up*/
				case DIO_PORT_INPUT_PULLUP :
					DDRA = 0;
					PORTA = 0xff;
					break ;
			}
			break ;

		/*in case of setting the direction of port B*/
		case DIO_PORTB :

			/*switch over different directions*/
			switch(Copy_u8PortDirection)
			{
				/*in case of setting the Port to be output*/
				case DIO_PORT_OUTPUT :
					DDRB = 0xff;
					break ;

				/*in case of setting the Port to be input float*/
				case DIO_PORT_INPUT_FLOAT :
					DDRB = 0;
					PORTB = 0;
					break ;

				/*in case of setting the Port to be input pull up*/
				case DIO_PORT_INPUT_PULLUP :
					DDRB = 0;
					PORTB = 0xff;
					break ;
			}
			break ;

		/*in case of setting the direction of port C*/
		case DIO_PORTC :

			/*switch over different directions*/
			switch(Copy_u8PortDirection)
			{
				/*in case of setting the Port to be output*/
				case DIO_PORT_OUTPUT :
					DDRC = 0xff;
					break ;

				/*in case of setting the Port to be input float*/
				case DIO_PORT_INPUT_FLOAT :
					DDRC = 0;
					PORTC = 0;
					break ;

				/*in case of setting the Port to be input pull up*/
				case DIO_PORT_INPUT_PULLUP :
					DDRC = 0;
					PORTC = 0xff;
					break ;
			}
			break ;

		/*in case of setting the direction of port D*/
		case DIO_PORTD :

			/*switch over different directions*/
			switch(Copy_u8PortDirection)
			{
				/*in case of setting the Port to be output*/
				case DIO_PORT_OUTPUT :
					DDRD = 0xff;
					break ;

				/*in case of setting the Port to be input float*/
				case DIO_PORT_INPUT_FLOAT :
					DDRD = 0;
					PORTD = 0;
					break ;

				/*in case of setting the Port to be input pull up*/
				case DIO_PORT_INPUT_PULLUP :
					DDRD = 0;
					PORTD = 0xff;
					break ;
			}
		break ;
		}
}

/****************************************************************************************************/
/****************************************************************************************************/

u8 DIO_u8SetPortValue(u8 Copy_u8PortID  , u8 Copy_u8PortValue)
{
	/*This local variable is for error reporting*/
	/*Initially error state = 0(OK)*/
	u8 Local_u8errorstate = 0;
	if(Copy_u8PortValue >= 0 || Copy_u8PortValue <= 255)
	{
	    /*switching over ports*/
		switch(Copy_u8PortID)
		{

					/*in case of setting the Value of port A*/
					case DIO_PORTA :
						PORTA = Copy_u8PortValue;
						break ;

					/*in case of setting the Value of port B*/
					case DIO_PORTB :
						PORTB = Copy_u8PortValue;
						break ;

					/*in case of setting the Value of port C*/
					case DIO_PORTC :
						PORTC = Copy_u8PortValue;
						break ;

					/*in case of setting the Value of port D*/
					case DIO_PORTD :
						PORTD = Copy_u8PortValue;
						break ;

					default:
						/*In case of invalid port id*/
						Local_u8errorstate = 1;
						break;

		}
	}
	else
	{
		/*In case of invalid value*/
		Local_u8errorstate = 2;
	}

	return Local_u8errorstate ;
}

/****************************************************************************************************/
/****************************************************************************************************/

void DIO_voidTogglePin(u8 Copy_u8PortID , u8 Copy_u8Pin)
{
	    /*switching over ports*/
		switch(Copy_u8PortID)
		{
			/*in case of Toggling the Value of a pin in port A*/
			case DIO_PORTA :
				TOG_BIT(PORTA , Copy_u8Pin);
				break ;

			/*in case of Toggling the Value of a pin in port B*/
			case DIO_PORTB :
				TOG_BIT(PORTB , Copy_u8Pin);
				break ;

			/*in case of Toggling the Value of a pin in port C*/
			case DIO_PORTC :
				TOG_BIT(PORTC , Copy_u8Pin);
				break ;

			/*in case of Toggling the Value of a pin in port D*/
			case DIO_PORTD :
				TOG_BIT(PORTD , Copy_u8Pin);
				break ;
		}
}

/****************************************************************************************************/
/****************************************************************************************************/

u8 DIO_u8GetPinValue(u8 Copy_u8PortID , u8 Copy_u8Pin)
{
	u8 Local_u8PinValue;
	/*switching over ports*/
		switch(Copy_u8PortID)
		{
			/*in case of Getting the value of a pin in port A*/
			case DIO_PORTA :
				Local_u8PinValue = GET_BIT(PINA , Copy_u8Pin);
				break ;

			/*in case of Getting the value of a pin in port B*/
			case DIO_PORTB :
				Local_u8PinValue = GET_BIT(PINB , Copy_u8Pin);
				break ;

			/*in case of Getting the value of a pin in port C*/
			case DIO_PORTC :
				Local_u8PinValue = GET_BIT(PINC , Copy_u8Pin);
				break ;

			/*in case of Getting the value of a pin in port D*/
			case DIO_PORTD :
				Local_u8PinValue = GET_BIT(PIND , Copy_u8Pin);
				break ;
		}
	return Local_u8PinValue;
}

'''

ADC_Interface='''

/*************************************************************************/
/*************************Interfacing macros******************************/
/*************************************************************************/

#define CHANNEL_0 0
#define CHANNEL_1 1
#define CHANNEL_2 2
#define CHANNEL_3 3
#define CHANNEL_4 4
#define CHANNEL_5 5
#define CHANNEL_6 6
#define CHANNEL_7 7

/*************************************************************************/
/*************************Functions' prototypes****************************/
/*************************************************************************/

/*This function is for initializing ADC peripheral*/
void ADC_voidInit(void);

/*This function shall start conversion Using Interrupts ASYNC*/
void ADC_voidStartConversionAsync(u8 Copy_u8Channel , u8 * Copy_u8Reading);

/*This function shall start conversion without Using Interrupts SYNC*/
//u8 ADC_u8StartConversionsync(u8 Copy_u8Channel);

/*This function is for CallBack*/
void ADC_voidSetCallBack(void(* Copy_PtrToFunction)(void));

'''

ADC_Configuration='''

/*Select the Vref:
 * 1- AVCC
 * 2- AREF
 * 3- INTERNAL (2.56V)*/

#define REF_VOLTAGE AVCC

/*Select Resolution
 * 1- BIT_8
 * 2- BIT_10*/

#define ADC_RESOLUTION BIT_8

/*Select Prescaler
 * 1- PRESCALER_2
 * 2- PRESCALER_4
 * 3- PRESCALER_8
 * 4- PRESCALER_16
 * 5- PRESCALER_32
 * 6- PRESCALER_64
 * 7- PRESCALER_128*/

#define PRESCALER PRESCALER_128

'''

ADC_Private='''

/******************************************Configuration Macros******************************************/

/*Vref Selections*/
#define AVCC	 0
#define AREF	 1
#define INTERNAL 2

/*Resolution Selections*/
#define BIT_8  0
#define BIT_10 1

/*Prescaler Selections*/
#define PRESCALER_2		0
#define PRESCALER_4		1
#define PRESCALER_8 	2
#define PRESCALER_16 	3
#define PRESCALER_32	4
#define PRESCALER_64	5
#define PRESCALER_128	6
/******************************************Private Macros******************************************/

#define MUX_MASK  		0b11100000
#define PRESCALER_MASK  0b11111000

/******************************************ADC registers******************************************/

#define ADMUX    *((volatile u8 *)(0x27))      //ADC multiplexer selection register
#define ADMUX_REFS1                   7         //for reference voltage selection bit1
#define ADMUX_REFS0                   6         //for reference voltage selection bit0
#define ADMUX_ADLAR                   5         //for left adjustment


#define ADCSRA   *((volatile u8 *)(0x26))      //ADC control and status registerA
#define ADCSRA_ADEN                   7         //for ADC enable
#define ADCSRA_ADSC                   6         //for ADC start conversion
#define ADCSRA_ADATE                  5         //for ADC auto trigger enable
#define ADCSRA_ADIF                   4         //for ADC interrupt flag
#define ADCSRA_ADIE                   3         //for ADC interrupt enable
#define ADCSRA_ADP2                   2         //for ADC clock prescaler bit 2
#define ADCSRA_ADP1                   1         //for ADC clock prescaler bit 1
#define ADCSRA_ADP0                   0         //for ADC clock prescaler bit 0

#define ADCH     *((volatile u8 *)(0x25))      //ADC high register
#define ADCL     *((volatile u8 *)(0x24))      //ADC low register

#define SFIOR    *((volatile u8 *)(0x50))      //ADC special function IO register
#define ADCR     *((volatile u16*)(0x24))      //ADC data register for 10 bit resolution

'''

ADC_Program='''

#include "../../LIB/LIB_STD_TYPES.h"
#include "../../LIB/LIB_BIT_MATH.h"

#include "../GIE/GIE_Interface.h"

#include "ADC_interface.h"
#include "ADC_private.h"
#include "ADC_configure.h"

/****************************************************************************************/
/************************************Global Variables************************************/
/****************************************************************************************/

/*Global pointer to function to set end of conversion interrupt call back*/
void(*Global_ptrEndOfConversion)(void) = NULL ;

/*Global pointer to u8 to receive the reading*/
u8 * ADC_u8GlobalReading = NULL ;

/***********************************************************************************************/
/***********************************Functions' Implementation***********************************/
/***********************************************************************************************/

void ADC_voidInit(void)
{
	/*Set reference voltage*/
	#if REF_VOLTAGE == AREF
		CLR_BIT(ADMUX , ADMUX_REFS0);
		CLR_BIT(ADMUX , ADMUX_REFS1);
	#elif REF_VOLTAGE == AVCC
		SET_BIT(ADMUX , ADMUX_REFS0);
		CLR_BIT(ADMUX , ADMUX_REFS1);
	#elif REF_VOLTAGE == INTERNAL
		SET_BIT(ADMUX , ADMUX_REFS0);
		SET_BIT(ADMUX , ADMUX_REFS1);
	#else
		#error"Wrong Reference Voltage Input"
	#endif

	/*Set Resolution*/
	#if ADC_RESOLUTION == BIT_8
		SET_BIT(ADMUX , ADMUX_ADLAR); //Left Adjusted - Read ADCH
	#elif ADC_RESOLUTION == BIT_10
		SET_BIT(ADMUX , ADMUX_ADLAR); //Left Adjusted - Read ADCR
	#else
		#error"Wrong Resolution Input"
	#endif

	/*Set clock prescaler*/
	#if PRESCALER == PRESCALER_2
		CLR_BIT(ADCSRA,0);
		CLR_BIT(ADCSRA,1);
		CLR_BIT(ADCSRA,2);
	#elif PRESCALER == PRESCALER_4
		CLR_BIT(ADCSRA,0);
		SET_BIT(ADCSRA,1);
		CLR_BIT(ADCSRA,2);
	#elif PRESCALER == PRESCALER_8
		SET_BIT(ADCSRA,0);
		SET_BIT(ADCSRA,1);
		CLR_BIT(ADCSRA,2);
	#elif PRESCALER == PRESCALER_16
		CLR_BIT(ADCSRA,0);
		CLR_BIT(ADCSRA,1);
		SET_BIT(ADCSRA,2);
	#elif PRESCALER == PRESCALER_32
		SET_BIT(ADCSRA,0);
		CLR_BIT(ADCSRA,1);
		SET_BIT(ADCSRA,2);
	#elif PRESCALER == PRESCALER_64
		CLR_BIT(ADCSRA,0);
		SET_BIT(ADCSRA,1);
		SET_BIT(ADCSRA,2);
	#elif PRESCALER == PRESCALER_128
		SET_BIT(ADCSRA,0);
		SET_BIT(ADCSRA,1);
		SET_BIT(ADCSRA,2);
	#else
		#error "Wrong Prescaler Input"
	#endif

	/*Enable ADC*/
	SET_BIT(ADCSRA , ADCSRA_ADEN);
}


void ADC_voidStartConversionAsync(u8 Copy_u8Channel , u8 * Copy_u8Reading)
{
	/*Enable end of conversion interrupt*/
	SET_BIT(ADCSRA , ADCSRA_ADIE);

	/*Enable global interrupt*/
	GIE_voidEnableGlobal();

	/*Set ADC Channel (Bit Masking)*/
	ADMUX &= MUX_MASK ;
	ADMUX |= Copy_u8Channel ;

	/*Assign global variable to get the reading*/
	ADC_u8GlobalReading = Copy_u8Reading ;

	/*Start Conversion*/
	SET_BIT(ADCSRA , ADCSRA_ADSC);
}

u8 ADC_u8StartConversionsync(u8 Copy_u8Channel)
{
    /*Creating Local Var to Save the reading*/
	u8 Local_u8Reading = 0;

	/*Set ADC Channel (Bit Masking)*/
	ADMUX &= MUX_MASK ;
	ADMUX |= Copy_u8Channel ;

	/*Start Conversion*/
	SET_BIT(ADCSRA , ADCSRA_ADSC);

	/*Polling over the End Conversion Flag*/
	while(GET_BIT(ADCSRA , ADCSRA_ADIF));

	/*Reading ADC Value*/
	#if ADC_RESOLUTION == BIT_8
	Local_u8Reading = ADCH ; //Left Adjusted - Read ADCH
	#elif ADC_RESOLUTION == BIT_10
	Local_u8Reading = ADCR ; //Left Adjusted - Read ADCR
	#else
		#error"Wrong Resolution Input"
	#endif

	return Local_u8Reading;
}

void ADC_voidSetCallBack(void(*Copy_ptrToFunction)(void))
{
	if(Copy_ptrToFunction != NULL)
	{
		Global_ptrEndOfConversion = Copy_ptrToFunction ;
	}
}

void __vector_16(void) __attribute__((signal));
void __vector_16(void)
{
	if(Global_ptrEndOfConversion != NULL)
	{
		/*Reading ADC Value*/
		#if ADC_RESOLUTION == BIT_8
			*ADC_u8GlobalReading = ADCH ; //Left Adjusted - Read ADCH
		#elif ADC_RESOLUTION == BIT_10
			*ADC_u8GlobalReading = ADCR ; //Left Adjusted - Read ADCR
		#else
			#error"Wrong Resolution Input"
		#endif

		Global_ptrEndOfConversion();
	}
	else
	{
		/*do nothing*/
	}
}

'''



def Create_Module():

    f1 = open(ModuleName+"_interface.h" , "x")  #create Interface H File
    f2 = open(ModuleName+"_config.h" , "x")     #create Configuration H File
    f3 = open(ModuleName+"_private.h" , "x")    #create Private H File
    f4 = open(ModuleName+"_Program.c" , "x")    #create Program C File

    f1 = open(ModuleName+"_interface.h" , "a+") #Open Interface H File to read it and append data
    f2 = open(ModuleName+"_config.h" , "a+")    #Open Configuration H File to read it and append data
    f3 = open(ModuleName+"_private.h" , "a+")   #Open private H File to read it and append data
    f4 = open(ModuleName+"_Program.c" , "a+")   #Open Program C File to read it and append data

    #Writting Header Guard to the Interface H File
    f1.write("#ifndef "+ModuleName+"_INTERFACE_H_\n")
    f1.write("#define "+ModuleName+"_INTERFACE_H_")
    f1.write(Interface)
    f1.write("#endif /* "+ModuleName+"_INTERFACE_H_ */")

    #Writting Header Guard to the Configuration H File
    f2.write("#ifndef "+ModuleName+"_CONFIGURATION_H_\n")
    f2.write("#define "+ModuleName+"_CONFIGURATION_H_")
    f2.write(Configuration)
    f2.write("#endif /* "+ModuleName+"_CONFIGURATION_H_ */")

    #Writting Header Guard to the private H File
    f3.write("#ifndef "+ModuleName+"_PRIVATE_H_\n")
    f3.write("#define "+ModuleName+"_PRIVATE_H_")
    f3.write(Private)
    f3.write("#endif /* "+ModuleName+"_PRIVATE_H_ */")
    
    #Writting C Code to the Program C File
    f4.write(Program)

    f1 = open(ModuleName+"_interface.h" , "r") #open Interface H File to read it and append string(s)
    f2 = open(ModuleName+"_config.h" , "r")    #open Configuration H File to read it and append string(s)
    f3 = open(ModuleName+"_private.h" , "r")   #open private H File to read it and append string(s)
    f4 = open(ModuleName+"_program.c" , "r")   #open Program C File to read it and append string(s)

    f1.close()              #open Interface H File
    f2.close()              #open Configuration H File
    f3.close()              #open private H File
    f4.close()              #open Program C File



while True:
    print("\nWelcome to the AVR Module Creator")
    print("1. DIO")
    print("2. ADC")
    print("3. Quit")

    # Ask the user for their choice
    choice = input("Enter your choice (1-3): ")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        ModuleName = 'DIO'
        Interface = DIO_Interface
        Configuration = DIO_Configuration
        Private = DIO_Private
        Program = DIO_Program
        Create_Module()
    elif choice == "2":
        ModuleName = 'ADC'
        Interface = ADC_Interface
        Configuration = ADC_Configuration
        Private = ADC_Private
        Program = ADC_Program
        Create_Module()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")



